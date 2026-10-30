"""Copy chosen stills into film/assets/img (EXIF-upright, optional rotate, max 2400px long side)."""
import os
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
PICKS = {  # out name: (contact-sheet folder, index, rotate degrees)
    "clouds_man":   ("Editorial_images", 40, 0),
    "deep_night":   ("Param_Generated_Images_April", 38, 0),
    "stretch_mint": ("Women_Sleepwear", 27, 270),
    "muscle_sleep": ("Men_Sleepwear", 11, 0),
    "longer_dark":  ("Editorial_images", 29, 0),
    "best_stretch": ("Editorial_images", 48, 0),
    "stack_sky":    ("Product_Shots", 154, 0),
    "fly_pink":     ("Product_Shots", 165, 0),
    "shorts_pink":  ("Product_Shots", 166, 0),
    "cloud_bed":    ("Women_Sleepwear", 3, 0),
}
# deep_night: a 1448 px wide strip, wide enough for the bottom-anchored zoom-out and clear of the AI sparkle mark (~x1990, y1990)
CROPS = {"deep_night": (300, 0, 1748, 2048)}
for name, (folder, idx, rot) in PICKS.items():
    rel = open(f"review/img_{folder}.txt", encoding="utf-8").read().splitlines()[idx].split("\t")[1]
    im = ImageOps.exif_transpose(Image.open(os.path.join("raw/Image Dump", rel))).convert("RGB")
    if rot: im = im.rotate(rot, expand=True)
    if name in CROPS: im = im.crop(CROPS[name])
    im.thumbnail((2400, 2400), Image.LANCZOS)
    im.save(f"film/assets/img/{name}.jpg", quality=92)
    print(name, im.size, rel)
