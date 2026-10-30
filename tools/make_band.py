"""Tall cloud band for vertical wipes, layered from the two keyed puffs over a soft white core."""
import random
import numpy as np
from PIL import Image
OUT = "film/assets/img/clouds"
W, H = 1080, 3400
rng = random.Random(7)
band = Image.new("RGBA", (W, H), (0, 0, 0, 0))
core = np.zeros((H, W, 4), np.uint8); core[..., :3] = (244, 246, 250)
y = np.arange(H); a = np.clip(np.minimum(y - 820, 2580 - y) / 320, 0, 1)
core[..., 3] = (a * 255).astype(np.uint8)[:, None]
band.alpha_composite(Image.fromarray(core, "RGBA"))
puffs = [Image.open(f"{OUT}/puff1.png"), Image.open(f"{OUT}/puff2.png")]
for row in range(15):
    cy = 380 + row * 190
    for k in range(3):
        p = puffs[(row + k) % 2]
        if rng.random() < 0.5: p = p.transpose(Image.FLIP_LEFT_RIGHT)
        if cy > H / 2 and rng.random() < 0.6: p = p.transpose(Image.FLIP_TOP_BOTTOM)
        w = int(rng.uniform(640, 980)); p = p.resize((w, int(p.height * w / p.width)), Image.LANCZOS)
        x = int(-260 + k * 430 + rng.uniform(-120, 120))
        band.alpha_composite(p, (max(-p.width + 1, x) if x >= 0 else 0, max(0, cy - p.height // 2)) if x >= 0 else (0, max(0, cy - p.height // 2)), (max(0, -x), 0) if x < 0 else (0, 0))
band.save(f"{OUT}/band.png", optimize=True); print("band", band.size)
