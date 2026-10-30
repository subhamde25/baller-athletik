"""Rows of 10 frames (67 ms apart) around each transition time: trans_sheet.py <video> <out.jpg> t1 t2 ..."""
import sys, subprocess, io
from PIL import Image, ImageDraw
vid, out, ts = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3:]]
W, H, N, STEP = 135, 240, 10, 1 / 15
sheet = Image.new("RGB", (W * N + 60, H * len(ts)), (25, 25, 25)); d = ImageDraw.Draw(sheet)
for r, t in enumerate(ts):
    d.text((4, r * H + 4), f"{t:.2f}", fill="yellow")
    for k in range(N):
        tt = max(0, t - 0.3 + k * STEP)
        png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{tt:.3f}", "-i", vid, "-frames:v", "1", "-vf", f"scale={W}:{H}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
        if png: sheet.paste(Image.open(io.BytesIO(png)), (60 + k * W, r * H))
sheet.save(out, quality=85)
