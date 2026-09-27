// Frame-accurate renderer: seeks the page's paused GSAP timeline frame by frame and
// pipes PNG screenshots into ffmpeg, so output never depends on realtime playback.
//
// Usage (run from the workdir that holds index.html):
//   node <skill>/scripts/render.cjs                          -> out.mp4 (full video)
//   node <skill>/scripts/render.cjs --stills 0.5,2.4,13.6    -> still-<t>.jpg per timestamp
//   node <skill>/scripts/render.cjs --out ad.mp4 --size 1080x1920 --fps 30 --channel chromium
//
// The page must expose window.seek(t), window.DURATION and window.ready (a Promise
// resolving once fonts and images are decoded), and skip autoplay when ?render is set.
const path = require('path')
const { spawn } = require('child_process')
const { chromium } = require('playwright-core')

const arg = (name, def) => {
  const i = process.argv.indexOf(`--${name}`)
  return i > -1 ? process.argv[i + 1] : def
}
const [W, H] = arg('size', '1080x1350').split('x').map(Number)
const FPS = Number(arg('fps', 30))
const OUT = arg('out', 'out.mp4')
const STILLS = arg('stills', null)
const CHANNEL = arg('channel', 'chrome')
const PAGE = path.resolve(arg('page', 'index.html'))

;(async () => {
  const browser = await chromium.launch({ channel: CHANNEL })
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 })
  await page.goto('file://' + PAGE + '?render')
  await page.evaluate(() => window.ready)
  // Font swap and image decode can land a frame after the promise resolves.
  await page.waitForTimeout(500)

  if (STILLS) {
    for (const t of STILLS.split(',')) {
      await page.evaluate(t => window.seek(t), Number(t))
      await page.screenshot({ path: `still-${t}.jpg`, quality: 85, type: 'jpeg' })
    }
    await browser.close()
    console.log(`wrote ${STILLS.split(',').length} stills`)
    return
  }

  const duration = await page.evaluate(() => window.DURATION)
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '15', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', OUT],
  { stdio: ['pipe', 'inherit', 'inherit'] })
  const total = Math.round(duration * FPS)
  for (let f = 0; f < total; f++) {
    await page.evaluate(t => window.seek(t), f / FPS)
    const buf = await page.screenshot({ type: 'png' })
    if (!ff.stdin.write(buf)) { await new Promise(resolve => ff.stdin.once('drain', resolve)) }
  }
  ff.stdin.end()
  await new Promise(resolve => ff.on('close', resolve))
  await browser.close()
  console.log(`wrote ${OUT} (${total} frames @ ${FPS}fps, ${W}x${H})`)
})()
