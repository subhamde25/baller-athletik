"""Word timings for the VO: python -I tools/transcribe.py <audio> <out.json>"""
import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", sys.argv[1], "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
m = WhisperModel("small.en", device="cpu", compute_type="int8")
segs, _ = m.transcribe(audio, word_timestamps=True,
    initial_prompt="Baller Athletik sleepwear, DeepSleep Technology.")
words = [{"id": f"w{i}", "text": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)}
         for i, w in enumerate(x for s in segs for x in s.words)]
json.dump(words, open(sys.argv[2], "w"), indent=1)
print(" ".join(f"{w['text']}@{w['start']}" for w in words))
