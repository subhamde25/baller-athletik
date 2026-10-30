"""Battery charge sound: five soft drop-warm ticks rising 0/+2/+4/+5/+7 semitones, 0.17 s apart,
one per battery segment (replaces the electronic 'full recharge' ping the user disliked in v1).

python -I tools/charge_ticks.py   (run from baller-athletik/)
"""
import subprocess

SRC = "assets/audio/sfx/drop-warm.mp3"
OUT = "film/assets/audio/sfx/charge-ticks.wav"
SEMIS, STEP = [0, 2, 4, 5, 7], 0.17

cmd = ["ffmpeg", "-v", "error", "-y"]
for _ in SEMIS:
    cmd += ["-i", SRC]
parts = []
for i, s in enumerate(SEMIS):
    rate, ms = 2 ** (s / 12), int(round(i * STEP * 1000))
    gain = 0.42 + 0.06 * i  # each step a touch brighter
    parts.append(f"[{i}:a]asetrate={int(48000 * rate)},aresample=48000,volume={gain:.2f},"
                 f"afade=t=out:st=0.25:d=0.15,adelay={ms}|{ms}[t{i}]")
parts.append("".join(f"[t{i}]" for i in range(len(SEMIS))) + f"amix=inputs={len(SEMIS)}:normalize=0,alimiter=limit=0.7[o]")
subprocess.run(cmd + ["-filter_complex", ";".join(parts), "-map", "[o]", "-ac", "2", "-ar", "48000", OUT], check=True)
print(OUT)
