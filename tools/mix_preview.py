"""Mix every <audio> in film/index.html offline and report loudness + where the peaks are.

python -I tools/mix_preview.py [out.wav]   (run from baller-athletik/)
"""
import re, subprocess, sys

html = open("film/index.html", encoding="utf-8").read()
tracks = []
for tag in re.findall(r"<audio [^>]+>", html):
    a = dict(re.findall(r'([\w-]+)="([^"]*)"', tag))
    tracks.append((a["id"], "film/" + a["src"], float(a.get("data-start", 0)), float(a.get("data-volume", 1))))

cmd = ["ffmpeg", "-v", "error", "-y"]
for _, src, _, _ in tracks:
    cmd += ["-i", src]
parts = []
for i, (_, _, start, vol) in enumerate(tracks):
    ms = int(round(start * 1000))
    parts.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,volume={vol},adelay={ms}|{ms}[a{i}]")
mix = "".join(f"[a{i}]" for i in range(len(tracks)))
parts.append(f"{mix}amix=inputs={len(tracks)}:normalize=0:duration=longest,atrim=0:32[m]")
out = sys.argv[1] if len(sys.argv) > 1 else "review/mix_preview.wav"
subprocess.run(cmd + ["-filter_complex", ";".join(parts), "-map", "[m]", out], check=True)

r = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True).stderr
print("\n".join(l.strip() for l in r.splitlines()[-12:] if any(k in l for k in ("I:", "LRA:", "Peak:"))))

import numpy as np
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", out, "-ac", "1", "-ar", "48000", "-f", "s16le", "-"], capture_output=True).stdout
x = np.abs(np.frombuffer(raw, np.int16).astype(float)) / 32768
win = 4800
peaks = [(i * 0.1, 20 * np.log10(x[i * win:(i + 1) * win].max() + 1e-9)) for i in range(len(x) // win)]
hot = sorted(peaks, key=lambda p: -p[1])[:8]
print("hottest 0.1 s windows:", ", ".join(f"{t:.1f}s {db:+.1f}dB" for t, db in sorted(hot)))
