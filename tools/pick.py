"""Sheet of picked images: pick.py out.jpg Folder:idx,idx Folder:idx ..."""
import sys, os
from PIL import Image, ImageDraw, ImageOps
Image.MAX_IMAGE_PIXELS = None
out = sys.argv[1]; items = []
for arg in sys.argv[2:]:
    folder, idxs = arg.rsplit(":", 1)
    lines = open(f"review/img_{folder}.txt", encoding="utf-8").read().splitlines()
    for i in idxs.split(","):
        rel = lines[int(i)].split("\t")[1]
        items.append((f"{folder[:10]}#{i}", os.path.join("raw/Image Dump", rel)))
T = 300; cols = 6; rows = (len(items) + cols - 1) // cols
sheet = Image.new("RGB", (cols * T, rows * (T + 16)), (40, 40, 40)); d = ImageDraw.Draw(sheet)
for k, (lab, p) in enumerate(items):
    im = Image.open(p); im.draft("RGB", (T * 2, T * 2)); im = ImageOps.exif_transpose(im).convert("RGB")
    w, h = im.size; im.thumbnail((T, T)); x, y = (k % cols) * T, (k // cols) * (T + 16)
    sheet.paste(im, (x + (T - im.width) // 2, y)); d.text((x + 3, y + T + 2), f"{lab} {w}x{h}", fill="yellow")
sheet.save(out, quality=85)
