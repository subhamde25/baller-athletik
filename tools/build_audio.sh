#!/bin/sh
# Build the three audio files the composition plays (run from baller-athletik/).
#   film/assets/audio/vo.wav          supplied VO + the Fish-cloned closing line, -16 LUFS
#   film/assets/audio/bgm.wav         the 32 s music edit: drop on "Baller", bar splice into the full section
#   film/assets/audio/sfx/charge-ticks.wav   five rising ticks for the battery
set -e
A=assets/audio
F=film/assets/audio
mkdir -p "$F/sfx"

# VO: the supplied read stops at "Upgrade your recovery." (27.36 s). Fish take 1 of
# "Try Baller Athletik today." (clone of the same voice, 143 Hz vs 147 Hz) follows after 0.40 s,
# 2.5 dB down to match the original tail, then the whole read is normalised.
ffmpeg -v error -y -i "$A/vo_supplied.mp3" -i "$A/tag/take1.mp3" -filter_complex \
  "[0:a]aresample=48000,atrim=0:27.40,afade=t=out:st=27.30:d=0.10,apad=pad_dur=0.40[a];\
   [1:a]aresample=48000,volume=-2.5dB,afade=t=in:d=0.01[b];\
   [a][b]concat=n=2:v=0:a=1,aformat=channel_layouts=mono,loudnorm=I=-16:TP=-1.5:LRA=11[o]" \
  -map "[o]" -ar 48000 "$A/vo_full.wav"
cp "$A/vo_full.wav" "$F/vo.wav"

# Music: bed B is 96 BPM with its drop on the downbeat at 10.12 s. Delay it 0.63 s so the drop
# lands on "Baller" (10.75 s), splice bar line 22.62 s -> 30.12 s so the fuller section carries
# the payoff (film 23.25 s), fade out over the end card.
ffmpeg -v error -y -i "$A/bgm/bed_B.mp3" -filter_complex \
  "[0:a]atrim=0:22.66,asetpts=PTS-STARTPTS[p1];[0:a]atrim=30.08:39.2,asetpts=PTS-STARTPTS[p2];\
   [p1][p2]acrossfade=d=0.06:c1=tri:c2=tri,adelay=630|630,atrim=0:32.0,\
   afade=t=in:st=0.63:d=0.25,afade=t=out:st=30.6:d=1.4,alimiter=limit=0.89[o]" \
  -map "[o]" -ar 48000 "$F/bgm.wav"

# Battery: one soft tick per segment (0.17 s apart), pitched 0/+2/+4/+5/+7 semitones.
python -I tools/charge_ticks.py

cp "$A"/sfx/*.mp3 "$F/sfx/"
echo "audio built"
