"""Tiles images into one labelled JPG so a whole set can be reviewed in a single Read.

Usage (from the workdir):
  python3 contact-sheet.py images a/web    -> images.jpg (every image in the folder, labelled by filename)
  python3 contact-sheet.py stills          -> stills.jpg (every still-*.jpg, time-sorted)
"""
import glob
import os
import sys
from PIL import Image, ImageDraw

mode = sys.argv[1] if len(sys.argv) > 1 else 'stills'

if mode == 'images':
    folder = sys.argv[2] if len(sys.argv) > 2 else 'a'
    files = sorted(f for f in glob.glob(os.path.join(folder, '*'))
                   if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')))
    W, H, cols = 240, 300, 6
    rows = max(1, (len(files) + cols - 1) // cols)
    sheet = Image.new('RGB', (W * cols, (H + 24) * rows), 'white')
    draw = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        x, y = (i % cols) * W, (i // cols) * (H + 24)
        try:
            im = Image.open(f).convert('RGB')
        except Exception:
            continue
        label = f'{os.path.basename(f)} {im.width}x{im.height}'
        im.thumbnail((W - 8, H - 8))
        sheet.paste(im, (x + 4, y + 4))
        draw.text((x + 6, y + H + 4), label, fill='black')
    sheet.save('images.jpg', quality=88)
    print(f'wrote images.jpg ({len(files)} images)')
else:
    files = sorted(glob.glob('still-*.jpg'), key=lambda f: float(f[6:-4]))
    W, H, cols = 432, 540, 5
    sheet = Image.new('RGB', (W * min(cols, max(1, len(files))), H * max(1, (len(files) + cols - 1) // cols)), 'white')
    draw = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        im = Image.open(f).convert('RGB')
        im.thumbnail((W, H))
        x, y = (i % cols) * W, (i // cols) * H
        sheet.paste(im, (x, y))
        draw.text((x + 6, y + 6), f[6:-4] + 's', fill='red')
    sheet.save('stills.jpg', quality=88)
    print(f'wrote stills.jpg ({len(files)} frames)')
