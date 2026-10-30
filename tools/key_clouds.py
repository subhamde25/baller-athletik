"""Key the black-background cloud renders into alpha PNGs for the film (run from baller-athletik/)."""
import numpy as np
from PIL import Image, ImageFilter
SRC, OUT = "assets/clouds_raw", "film/assets/img/clouds"

def key(path, boost=1.7, gamma=0.85, fit=1200):
    im = Image.open(path).convert("RGB")
    im.thumbnail((fit, fit), Image.LANCZOS)          # downscale first: this machine is short on RAM
    a = np.asarray(im).astype(np.float32) / 255
    lum = a.max(axis=2)
    alpha = np.clip((np.clip(lum - 0.03, 0, 1) / 0.97 * boost) ** gamma, 0, 1)
    rgb = np.clip(a / np.maximum(alpha[..., None], 1e-3), 0, 1)       # un-premultiply off black
    rgb = 0.15 + 0.85 * rgb                                            # lift shadows: clouds read light grey, not black
    return np.dstack([rgb, alpha])

def save(arr, name, max_side=None):
    im = Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8), "RGBA")
    bbox = im.getchannel("A").point(lambda v: 255 if v > 6 else 0).getbbox()
    im = im.crop(bbox)
    if max_side: im.thumbnail((max_side, max_side), Image.LANCZOS)
    im.save(f"{OUT}/{name}.png", optimize=True); print(name, im.size)
    return im

for n in ("puff1", "puff2"):
    save(key(f"{SRC}/{n}.png"), n, 1100)
save(key(f"{SRC}/stream.png", boost=2.2, fit=2200), "stream", 2200)

# tall band for vertical cloud wipes: billowy top + solid core + billowy bottom
bank = Image.fromarray((key(f"{SRC}/bank.png", boost=2.0, fit=1935) * 255).astype(np.uint8), "RGBA").resize((1080, 1935), Image.LANCZOS)
half = bank.crop((0, 380, 1080, 1935))
core_col = tuple(int(v) for v in np.asarray(half)[-40:, :, :3].reshape(-1, 3).mean(axis=0)) + (255,)
band = Image.new("RGBA", (1080, half.height * 2 + 260), (0, 0, 0, 0))
band.paste(half, (0, 0))
band.paste(Image.new("RGBA", (1080, 260), core_col), (0, half.height))
band.paste(half.transpose(Image.FLIP_TOP_BOTTOM), (0, half.height + 260))
# make sure the middle is fully opaque so the cut underneath never shows
arr = np.asarray(band).copy(); mid0, mid1 = half.height - 500, half.height + 760
arr[mid0:mid1, :, 3] = np.maximum(arr[mid0:mid1, :, 3], 255)
band = Image.fromarray(arr, "RGBA"); band.save(f"{OUT}/band.png", optimize=True); print("band", band.size, core_col)

# cloud-shaped window mask for the dream reveal (solid core, fluffy edge)
m = key(f"{SRC}/puff1.png", fit=1400)[..., 3]
m = np.clip((m - 0.12) * 2.6, 0, 1)
mask = np.zeros(m.shape + (4,), np.float32); mask[..., :3] = 1; mask[..., 3] = m
save(mask, "bubble_mask", 1400)

# --- polish: brighter clouds, soft white core in the band, feathered stream ends
def lift(path, amt):
    a = np.asarray(Image.open(path)).astype(np.float32) / 255
    a[..., :3] = 1 - (1 - a[..., :3]) * amt
    return a

b = lift(f"{OUT}/band.png", 0.45)
h = b.shape[0]; top, bot = 1555 - 360, 1555 + 260 + 360
for y in range(top, bot):                     # core: cool white fading into the cloud texture
    t = min(1.0, min(y - top, bot - y) / 300)
    b[y, :, :3] = b[y, :, :3] * (1 - t) + np.array([0.95, 0.96, 0.98]) * t
    b[y, :, 3] = 1
Image.fromarray((b * 255).astype(np.uint8), "RGBA").save(f"{OUT}/band.png", optimize=True)

s = lift(f"{OUT}/stream.png", 0.6)
w = s.shape[1]; ramp = np.clip(np.minimum(np.arange(w), w - 1 - np.arange(w)) / (w * 0.18), 0, 1)
s[..., 3] *= ramp[None, :]
Image.fromarray((s * 255).astype(np.uint8), "RGBA").save(f"{OUT}/stream.png", optimize=True)
print("polished band + stream")
