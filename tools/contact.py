"""Contact sheet per Image Dump top folder: python contact.py <root> <outdir>"""
import sys, os, glob
from PIL import Image, ImageDraw, ImageOps
Image.MAX_IMAGE_PIXELS = None
root, out = sys.argv[1], sys.argv[2]
T = 150
for d in sorted(os.listdir(root)):
    p = os.path.join(root, d)
    if not os.path.isdir(p): continue
    fs = [f for f in glob.glob(os.path.join(p, "**", "*"), recursive=True)
          if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not fs: continue
    cols = 10; rows = (len(fs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * T, rows * (T + 14)), (40, 40, 40)); dr = ImageDraw.Draw(sheet)
    for i, f in enumerate(sorted(fs)):
        try:
            im = Image.open(f); im.draft("RGB", (T * 2, T * 2)); im = ImageOps.exif_transpose(im).convert("RGB")
            im.thumbnail((T, T)); x, y = (i % cols) * T, (i // cols) * (T + 14)
            sheet.paste(im, (x + (T - im.width) // 2, y))
            dr.text((x + 2, y + T), f"{i}", fill="yellow")
        except Exception as e: print("bad", f, e)
    name = d.replace(" ", "_").replace("&", "and").replace("'", "")
    sheet.save(os.path.join(out, f"img_{name}.jpg"), quality=80)
    with open(os.path.join(out, f"img_{name}.txt"), "w", encoding="utf-8") as t:
        t.write("\n".join(f"{i}\t{os.path.relpath(f, root)}" for i, f in enumerate(sorted(fs))))
    print(d, len(fs))
