"""List PSD layers and export composite + each named pixel/smart layer to PNG."""
import sys, os, re
from psd_tools import PSDImage
src, out = sys.argv[1], sys.argv[2]
psd = PSDImage.open(src)
print(src, psd.width, psd.height)
psd.composite().save(os.path.join(out, "composite.png"))
for i, l in enumerate(psd.descendants()):
    print("  " * 0 + f"{i:3d} {l.kind:10s} vis={l.visible!s:5s} {l.bbox} {l.name}")
    if l.kind in ("pixel", "smartobject", "shape", "type") and l.width > 0:
        try:
            im = l.composite()
            if im: im.save(os.path.join(out, f"{i:03d}_{re.sub(r'[^A-Za-z0-9_-]+','_',l.name)[:40]}.png"))
        except Exception as e: print("    skip", e)
