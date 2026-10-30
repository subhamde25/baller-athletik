"""RMS dB per second + low/high band split: energy.py <audio>"""
import sys, subprocess, numpy as np
raw = subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-ac","1","-ar","22050","-f","s16le","-"],capture_output=True).stdout
a = np.frombuffer(raw,np.int16).astype(np.float32)/32768; sr=22050
out=[]
for s in range(0, len(a)//sr):
    x=a[s*sr:(s+1)*sr]; X=np.abs(np.fft.rfft(x)); f=np.fft.rfftfreq(len(x),1/sr)
    lo=20*np.log10(np.sqrt((X[(f<150)]**2).sum())/len(x)+1e-9); hi=20*np.log10(np.sqrt((X[(f>4000)]**2).sum())/len(x)+1e-9)
    rms=20*np.log10(np.sqrt((x**2).mean())+1e-9)
    out.append(f"{s:3d}s {rms:5.1f} lo{lo:5.0f} hi{hi:5.0f}")
for i in range(0,len(out),4): print(" | ".join(out[i:i+4]))
