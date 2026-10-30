# Assets

Every file the ad uses: where it came from, its status, how it was processed and where it lands.

**Storage:** committed are the final master (`deliverables/*.mp4`, Git LFS), the music beds and SFX
library, the cloud renders and their keyed cutouts, the SD watermark and the VO word timings. The
supplied Drive media (`raw/`), everything cut or extracted from it (`film/assets/img/*.jpg`,
`film/assets/video/`, the wordmark and DeepSleep® PNGs, `vo.wav`), review frames (`review/`) and
drafts (`renders/`) are not. `tools/` recreates them.

## 1. Supplied media (Adbuffs Drive, not committed)

`tools/drive_tree.py` lists the four public folders into `tools/drive_manifest.json` (689 files);
`tools/fetch_drive.py` downloads them to `raw/` (660 files, 4.6 GB; the 74 PSDs inside the image
folders are skipped).

### Footage → `film/assets/video/` (`tools/cut_clips.sh`)

16:9 stock is cropped to a 608×1080 window, Lanczos-upscaled to 1080×1920 with a light unsharp; the
4K vertical product clips are scaled down. All at 30 fps.

| Clip | Source (in, length) | Used |
|---|---|---|
| `hook_alarm` | stock "sleepy man turns off the alarm" (1.2 s, 3.2 s), window on the clock | 0–2.23 s |
| `wake_a` · `wake_b` · `wake_c` | stock "man waking up in the middle of the night" (5.4 / 7.6 / 12.4 s) | tired · sore · problem |
| `stretch` | stock "man raising his hands and stretching" (2.9 s) | energized |
| `brand_model` | `C3035_1.mp4` 4K (9.4 s) | brand reveal |
| `waistband` | `C3040_1.mp4` 4K (0.2 s) | DeepSleep® |
| `sleeve` | `C3037_1.mp4` 4K (0.3 s) | spare (not in the cut) |

### Stills → `film/assets/img/` (`tools/prep_stills.py`)

| Still | Source | Treatment | Used |
|---|---|---|---|
| `clouds_man` | Editorial images / Man sleeping on clouds Navy & Beige | natural-aspect box, bottom-anchored zoom-out, sky fill above | recovers |
| `deep_night` | Param Generated Images April / Ad 6 / Gemini_Generated_Image_5digft… | cropped x 300–1748 (clears the AI sparkle mark), night grade | sleep deeper |
| `stretch_mint` | Women_Sleepwear / PHD00108 copy 2 colour corrected copy | rotated 270° (overhead shot), sheet fill above | recover faster |
| `muscle_sleep` | Men Sleepwear / PrettyGuy_Sleepwear | bottom-anchored, pillow-dark fill above | relax muscles |
| `longer_dark` | Editorial images / Forest green Tee Man sleeping on bed | object-position 68% | deep sleep longer |
| `cloud_bed` | Women_Sleepwear / Bedskyclouds&Abeer | object-position 41% | feeling your… |
| `best_stretch` | Editorial images / Women Blush shorts set | — | best. |
| `stack_sky` | Product Shots / MenStackCloudy | object-position 50% 60% | Upgrade your sleepwear |
| `fly_pink` | Product Shots / Pink womens set | — | Upgrade your recovery |
| `shorts_pink` | Product Shots / Pink_freepik__keep-the-2nd-image… | radial mask into a matching sky gradient | end card |

### Brand marks → `film/assets/brand/` (`tools/extract_brand.py`)

| File | Source | Treatment |
|---|---|---|
| `wordmark_black.png` / `_white` | `Task 18.psd` layer 8 (568×70) | alpha ×4 Lanczos, blur 1.2, re-thresholded → 2272×280 |
| `deepsleep_black.png` / `_white` | `Task 18.psd` smart object "SeepSleep Technology Logo Unit copy" (2000×388 PNG) | recoloured |

### Voice-over

| File | Source | Treatment |
|---|---|---|
| `assets/audio/vo_supplied.mp3` | Additional Assets / `ElevenLabs_…Baller Athletik-Male….mp3` (27.6 s) | trimmed at 27.40 s |
| `assets/audio/tag/take1.mp3` | Fish Audio TTS, private clone "Baller Athletik Male VO" (voice id `dce6392658f147b3aae653292fee5ef7`, cloned from the supplied read) | "Try Baller Athletik today."; take 1 of 3 (pitch 143 Hz vs the original's 147 Hz), −2.5 dB |
| `film/assets/audio/vo.wav` | both joined with a 0.40 s gap (`tools/build_audio.sh`) | loudnorm −16 LUFS / −1.5 dBTP, 29.3 s, placed at 0.25 s |
| `film/assets/transcript-words.json` | faster-whisper `small.en` on `vo.wav` (`tools/transcribe.py`) | 81 words; drives every caption |

## 2. Generated for this project (committed)

| File | Made with | Use |
|---|---|---|
| `assets/audio/bgm/bed_B.mp3` (61 s) | Runway music: "hushed and nocturnal … opens up into a warm, hopeful, sunrise feel around 10 s … 96 BPM" | the music bed (`bgm.wav`) |
| `assets/audio/bgm/bed_A.mp3` (106 s) | Runway music, alternative prompt | not used |
| `alarm` · `rustle` · `pulse` · `shimmer` · `charge` (`assets/audio/sfx/`) | Runway sound effects | alarm, waking, circulation, DeepSleep® (`charge` was replaced in v2) |
| `film/assets/audio/sfx/charge-ticks.wav` | `tools/charge_ticks.py` from `drop-warm.mp3` | battery |
| `assets/clouds_raw/bank.png` · `puff1.png` · `puff2.png` · `stream.png` | Runway images (white clouds on pure black, 2K) | cloud transitions |
| `film/assets/img/clouds/*.png` | `tools/key_clouds.py` (brightness → alpha, un-premultiplied, lifted) + `tools/make_band.py` (15 rows of puffs over a solid white core, 1080×3400) | wipes, fly-throughs, drifting layers, dream-bubble mask |

## 3. SFX library (`assets/audio/sfx/`, the author's own)

`swoosh-air`, `push-whoosh`, `dive-whoosh`, `iris-whoosh`, `pop`, `brand-twinkle`, `light-shimmer`,
`impact-bass-1`, `glass-ting`, `panel-flick`, `rise-into-logo`, `click-soft` (from the BRAINR library)
and `pencil-sketch`, `drop-warm` (from the Beaklet library). Placement and gains are in
[`BREAKDOWN.md`](../BREAKDOWN.md#sound-cue-sheet-v3).

## 4. Type and marks

| File | Source / licence | Use |
|---|---|---|
| Inter, Playfair Display | bundled with HyperFrames (SIL OFL 1.1) | captions, end card |
| `film/assets/brand/sd-watermark-white.png` · `sd-watermark-navy.png` | the author's SD mark (1781×1320) | top-right, 84 px, 60% |
