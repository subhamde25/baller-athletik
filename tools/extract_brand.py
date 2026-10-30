"""Pull the brand marks out of the supplied Task 18.psd into film/assets/brand/.

python -I tools/extract_brand.py   (run from baller-athletik/, needs psd-tools)

- Layer 8 is the BALLER|ATHLETIK wordmark, only 568x70 px: its alpha is upscaled 4x, softened and
  re-thresholded so the edges stay crisp at 880 px, then written in ink and white.
- The hidden smart object "SeepSleep Technology Logo Unit copy" embeds a 2000x388 PNG of the
  DeepSleep(R) Technology lockup; it is recoloured to ink and white.
"""
import io
import numpy as np
from PIL import Image, ImageFilter
from psd_tools import PSDImage

PSD = "raw/Additional Assets/Task 18.psd"
OUT = "film/assets/brand"
INK, WHITE = (17, 17, 17), (255, 255, 255)

psd = PSDImage.open(PSD)
layers = list(psd.descendants())

mark = layers[8].composite().convert("RGBA")
a = np.array(mark)[:, :, 3]
big = Image.fromarray(a).resize((mark.width * 4, mark.height * 4), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
b = np.clip((np.array(big).astype(float) - 128) * 4 + 128, 0, 255).astype("uint8")  # ~1.5 px anti-aliased edge
for name, col in (("wordmark_black", INK), ("wordmark_white", WHITE)):
    o = np.zeros(b.shape + (4,), "uint8"); o[..., :3] = col; o[..., 3] = b
    Image.fromarray(o).save(f"{OUT}/{name}.png")

so = next(l for l in layers if l.kind == "smartobject" and "Logo" in l.name).smart_object
lock = np.array(Image.open(io.BytesIO(so.data)).convert("RGBA"))
for name, col in (("deepsleep_black", INK), ("deepsleep_white", WHITE)):
    o = lock.copy(); o[..., :3] = col
    Image.fromarray(o).save(f"{OUT}/{name}.png")
print("wordmark", b.shape[::-1], "lockup", lock.shape[1::-1])
