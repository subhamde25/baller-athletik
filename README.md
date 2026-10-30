# Baller Athletik — "DeepSleep®" Meta ad

A 32-second vertical (9:16) Meta video ad for **Baller Athletik** sleepwear, made for the **Adbuffs**
design test. Built in [HyperFrames](https://hyperframes.heygen.com) (HTML + GSAP) from the brand's
supplied footage, photography and voice-over, with Python + ffmpeg prep and an original music bed,
rendered to 1080×1920 at 30 fps.

| | |
|---|---|
| **Final cut** | [`deliverables/Baller_Athletik_DeepSleep_MetaAd_1080x1920_SD_v3.mp4`](deliverables/) (1080×1920, 30 fps, 32.0 s, −15.7 LUFS, −1.5 dBTP, Git LFS) |
| **Copy** | the brief's fixed script, word for word: "Think sleep is just about the hours? Nope…" → "Try Baller Athletik today." |
| **Story** | problem (cool, grey stock footage: tired, sore, the sleepwear is the problem) → a warm light-leak "wake-up" into the brand world → DeepSleep® benefits, each with its own visual metaphor → upgrade → end card |
| **Style** | matched to the two reference ads: small Inter line + one huge Playfair Display Italic hero word, clouds and sky, battery / vessels / hypnogram graphics, light leaks, whips, spins and cloud transitions |
| **Grade** | problem world cool and desaturated (temp −0.18, sat −0.35, blue shadows); brand world warm daylight; night shots cool blue |
| **Voice** | the supplied ElevenLabs male read; its missing last line voiced with a private Fish Audio clone of the same voice |
| **Music & SFX** | original 96 BPM bed (drop on "Baller"), 26 cues each tied to an event on screen |
| **Safe zone** | every word between y 270 and 1250 (Meta Reels/Stories UI) |
| **Watermark** | SD mark, top-right, navy on light frames and white on dark ones |

> The brief and supplied assets are in [`BRIEF.md`](BRIEF.md). The reference study, beat sheet and
> sound cue sheet are in [`BREAKDOWN.md`](BREAKDOWN.md). Every asset's source and treatment is in
> [`docs/ASSETS.md`](docs/ASSETS.md); the pipeline, version history and gotchas are in
> [`docs/PRODUCTION.md`](docs/PRODUCTION.md).

## The ad in one glance

| Time | Beat | What happens |
|---|---|---|
| 0–3 s | **Hook** | "Think sleep is just about the *hours?*" over an alarm clock, a sleep arc sweeping 10 → 6 o'clock. "*Nope.*" strikes out "8 HOURS" |
| 3–6 s | **Reframe** | a dream cloud opens into a man asleep on clouds: "your body *recovers* while you rest" |
| 6–10.7 s | **Problem** | the camera falls through clouds into a dark bedroom: *tired? sore?* "Your sleepwear might be the *problem.*" |
| 10.7–14 s | **Reveal** | warm light leak, the music drops: BALLER\|ATHLETIK wordmark, a ring burst into the DeepSleep® waistband |
| 14–22.8 s | **Benefits** | sleep *deeper* (night clouds, Zzz), recover *faster* (whip, streaks), wake up *energized* (battery), *circulation* (vessel macro), relax *muscles* (calm wave), deep sleep *longer* (hypnogram) |
| 22.8–28 s | **Payoff** | rising through clouds: "feeling your *best.*", "Upgrade your *sleepwear.* → *recovery.*" |
| 28–32 s | **CTA** | pink shorts on sky, wordmark, DeepSleep®, "Try Baller Athletik *today.*", SHOP NOW |

## Project layout

```
baller-athletik/
├── film/                       # the HyperFrames project
│   ├── index.html              # root: 6 scene hosts, fx overlay, captions, watermark, VO + music + 26 SFX
│   ├── compositions/           # problem · brand · benefits · science · payoff · endcard · fx · captions · watermark
│   ├── SPEC.md                 # shot list with numbers (look, motion, safe zone, v3 transitions)
│   └── assets/
│       ├── img/clouds/         # keyed cloud cutouts (puffs, wipe band, stream, bubble mask)
│       ├── audio/              # bgm.wav, sfx/ (vo.wav is built, not committed)
│       ├── brand/              # SD watermarks (wordmark + DeepSleep are extracted, not committed)
│       ├── img/*.jpg · video/  # stills and clips cut from the supplied media          [not in repo]
│       └── transcript-words.json   # VO word timings (faster-whisper)
├── assets/
│   ├── audio/bgm/              # the two generated music beds (B is used)
│   ├── audio/sfx/              # SFX library
│   └── clouds_raw/             # the four cloud renders on black, before keying
├── tools/                      # the build pipeline (see docs/PRODUCTION.md)
├── deliverables/               # final master (v3)                                     [Git LFS]
├── docs/ASSETS.md · docs/PRODUCTION.md
├── raw/ · review/ · renders/   # Drive downloads, contact sheets, drafts                [not in repo]
└── BRIEF.md · BREAKDOWN.md
```

## Rebuild

```sh
python -I tools/fetch_drive.py tools/drive_manifest.json raw    # the supplied Drive folders → raw/
python -I tools/extract_brand.py                                 # wordmark + DeepSleep® from Task 18.psd
sh tools/cut_clips.sh && python -I tools/prep_stills.py          # 9:16 clips and stills → film/assets/
sh tools/build_audio.sh                                          # vo.wav, bgm.wav, charge ticks
python -I tools/make_captions.py                                 # film/compositions/captions.html
python -I tools/mix_preview.py                                   # check loudness and true peak first
cd film && npx hyperframes check && HF_SEGMENTED_CAPTURE=true npx hyperframes render --fps 30 \
  --quality delivery --workers 2 --no-low-memory-mode --protocol-timeout 900000 --resume -o ../renders/out.mp4
```

Needs Python 3.12 with numpy, Pillow, psd-tools and faster-whisper, plus ffmpeg and Node.js
(HyperFrames 0.8.x). `assets/audio/vo_supplied.mp3` and the Fish take `assets/audio/tag/take1.mp3`
come from the Drive folder and Fish Audio (see `docs/ASSETS.md`).

## Rights

Baller Athletik's footage, photography, voice-over and brand marks belong to Baller Athletik and
were supplied by Adbuffs for this test; none of that source media is committed, and the brief does
not permit portfolio use of the finished ad. The music, the generated SFX and the cloud art were
generated for this project; the SD watermark is the author's own.
