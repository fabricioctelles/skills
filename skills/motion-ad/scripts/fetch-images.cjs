// Downloads the real imagery a product page shows (product shots, customer examples,
// screenshots) so the ad uses genuine assets instead of invented ones.
//
// Usage (run from the workdir):
//   node <skill>/scripts/fetch-images.cjs --url https://example.com
//   node <skill>/scripts/fetch-images.cjs --url https://example.com/pricing --min 300 --limit 40 --out a/web
//
// Scrolls the page to trigger lazy loading, collects <img> and srcset sources whose
// rendered or natural width is at least --min px, and saves them as <out>/NN.<ext>
// with an index in <out>/images.json (src, alt, natural size).
// Downloads use curl with a browser user agent: many CDNs return 403 to default clients.
const fs = require('fs')
const path = require('path')
const { execFileSync } = require('child_process')
const { chromium } = require('playwright-core')

const arg = (name, def) => {
  const i = process.argv.indexOf(`--${name}`)
  return i > -1 ? process.argv[i + 1] : def
}
const URL = arg('url', null)
const MIN = Number(arg('min', 240))
const LIMIT = Number(arg('limit', 40))
const OUT = arg('out', 'a/web')
const CHANNEL = arg('channel', 'chrome')
if (!URL) { console.error('missing --url'); process.exit(1) }

;(async () => {
  const browser = await chromium.launch({ channel: CHANNEL })
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } })
  await page.goto(URL, { waitUntil: 'networkidle' })
  await page.evaluate(async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 700) {
      window.scrollTo(0, y)
      await new Promise(r => setTimeout(r, 250))
    }
  })
  await page.waitForTimeout(800)
  const found = await page.evaluate(min => {
    return [...document.images]
      .filter(img => Math.max(img.naturalWidth, img.getBoundingClientRect().width) >= min)
      .map(img => ({ src: img.currentSrc || img.src || '', alt: img.alt || '', width: img.naturalWidth, height: img.naturalHeight }))
      .filter(r => /^https?:/.test(r.src) && !/\.svg(\?|$)/i.test(r.src))
  }, MIN)
  await browser.close()

  const seen = new Set()
  const picked = found.filter(r => !seen.has(r.src) && seen.add(r.src)).slice(0, LIMIT)
  fs.mkdirSync(OUT, { recursive: true })
  const pad = n => String(n).padStart(2, '0')
  const saved = []
  picked.forEach((r, i) => {
    const ext = (path.extname(new globalThis.URL(r.src).pathname).toLowerCase().match(/\.(jpe?g|png|webp|avif|gif)$/) || ['.jpg'])[0]
    const file = path.join(OUT, `${pad(i)}${ext}`)
    try {
      execFileSync('curl', ['-sfL', '-A', 'Mozilla/5.0', '-o', file, r.src])
      saved.push({ file, ...r })
    } catch { console.error(`skipped ${r.src}`) }
  })
  fs.writeFileSync(path.join(OUT, 'images.json'), JSON.stringify(saved, null, 2))
  console.log(`downloaded ${saved.length} images to ${OUT}/ (of ${found.length} found)`)
})()
