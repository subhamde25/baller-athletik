# Breakdown

## Reference study

Both reference ads were cut-detected (frame-difference spikes) and every cut sampled as a strip of
10 frames 67 ms apart (`tools/trans_sheet.py` → `review/ref/`). Besides hard cuts they use:

| Reference | Technique | Used here |
|---|---|---|
| Task 19 0.8 s | the shot shrinks into a fluffy cloud-shaped "dream bubble" with trailing thought puffs; tilt down to the dreamer | **3.0 s** dream cloud: puffs pop, the cloud window opens out of the "Nope." card |
| Task 19 3.75 s | a cloud bank rushes up through frame with vertical motion blur | **5.95 s** cloud fall · **22.83 s** cloud rise (reversed) |
| Task 19 6.4 s | a white ring bursts from a point, a circle reveals the next shot | **12.6 s** ring burst into the DeepSleep waistband |
| Task 19 8.3 s | white rounded panel / X-mask wipes | — (one shape wipe is enough) |
| Task 19 13.4 s, Task 20 20.6 s | spin + zoom blur into a macro | **18.37 s** spin into the blood vessels |
| Task 19 15.9 s, 19.4 s; Task 20 6.6 s | vertical whip pans with heavy motion blur | **15.73 s** vertical whip (SVG y-only blur) |
| Task 19 11.1 s, 24 s; Task 20 3.4 s, 7.9 s | warm light-leak / film-burn flashes | **10.3 s** wake-up leak + flash · **16.83 s** film burn · **23.87 s** flash on "best." |
| Task 20 24.8 s, 26.3 s | heavy blur dissolves | **19.95 s** focus pull · **25.25 s** blur dissolve |
| Task 19, Task 20 | battery charging, blood vessels, muscle macro, Zzz, puzzle "RECOVER" | battery (5 segments + 100%), drawn vessel macro with flowing cells, Zzz, hypnogram, tension→calm wave |
| Task 19 | small grotesk line + one huge serif-italic hero word in sky blue | Inter 600 50 px + Playfair Display Italic 700 up to 186 px |
| Task 20 | bold problem → solution arc ("tired, sore, irritated" → product) | the same arc, carried by the brief's copy |
| both | end on a sky-blue product hero + wordmark / SHOP NOW | pink shorts on sky, wordmark, DeepSleep®, "Try Baller Athletik *today.*", SHOP NOW |

## Beat sheet (v3)

VO starts at 0.25 s. Every caption word lands on its spoken word (`tools/make_captions.py`).

| Time | Words | Picture | Motion graphics / transition |
|---|---|---|---|
| 0.00–2.23 | "Think sleep is just about the **hours?**" | alarm clock at 6:00, hand reaching (stock), cool grade | sleep arc sweeps the dial 10 → 6 o'clock (8 h), moon → sun |
| 2.23–2.95 | "**Nope.**" | off-white type card | ghost "8 HOURS" struck through in red |
| 2.95–5.95 | "It's about how well your body **recovers** while you rest." | man asleep on clouds | dream cloud opens out of a sky-blue card; foreground clouds drift |
| 5.95 | — | — | **cloud fall** into the dark bedroom |
| 5.95–7.25 | "Waking up **tired?**" | man waking at night (stock), cool desaturated grade | — |
| 7.25–8.50 | "Muscles still **sore?**" | same, hunched | punch-in |
| 8.50–10.75 | "Your sleepwear might be the **problem.**" | slumped on the bed edge | red hand-drawn scribble; warm leak + white flash on the cut |
| 10.75–12.60 | "Baller Athletik sleepwear is made with" | 4K model in tee + shorts, warm grade | wordmark wipes in on "Baller"; music drops |
| 12.60–14.10 | "DeepSleep Technology," | waistband close-up | **ring burst** iris; DeepSleep® lockup wipes up; zoom through the black shorts |
| 14.10–15.83 | "designed to help you sleep **deeper,**" | man on night clouds | **night cloud fly-through**; Zzz rise; fog drifts |
| 15.83–16.83 | "recover **faster,**" | overhead stretch | **vertical whip** in; speed streaks |
| 16.83–18.37 | "and wake up **energized.**" | stretch at the window (stock) | **film burn**; battery fills red → green, 100% |
| 18.37–19.95 | "It helps improve **circulation,**" | drawn vessel macro, flowing cells | **spin + zoom** in |
| 19.95–20.85 | "relax **muscles,**" | relaxed arm, asleep | **focus pull**; jagged line under "muscles," eases into a calm wave |
| 20.85–22.83 | "and keep your body in deep sleep **longer,**" | man asleep in the dark | hypnogram draws, the deep plateau lights blue |
| 22.83 | — | — | **cloud rise** into the sky |
| 22.83–23.87 | "so you wake up feeling your" | woman stretching on a bed in the sky | foreground clouds |
| 23.87–25.25 | "**best.**" | woman stretching, warm window light | **flash** on "best." |
| 25.25–26.60 | "Upgrade your **sleepwear.**" | folded stack under a cloudy sky | **blur dissolve** |
| 26.60–28.00 | "Upgrade your **recovery.**" | pink set flying through clouds | **cloud drift** sideways; hero rolls sleepwear. → recovery.; clouds stream past |
| 27.55 | — | — | **bright cloud fly-through** into the end card |
| 28.00–32.00 | "Try Baller Athletik **today.**" | end card: pink shorts on sky | wordmark, DeepSleep®, swoosh under "today.", SHOP NOW with a shine, cloud bed drifting |

## Sound cue sheet (v3)

Each cue starts so its measured peak lands about a frame after the picture event.

| Start (s) | Cue | Gain | Cause |
|---|---|---|---|
| 0.00 | `alarm` | 0.40 | alarm clock (Runway) |
| 2.14 | `pop` | 0.45 | "Nope." |
| 2.70 | `swoosh-air` | 0.40 | dream cloud opens |
| 2.95 | `light-shimmer` | 0.12 | thought puffs |
| 5.47 | `swoosh-air` | 0.35 | cloud fall |
| 5.90 | `rustle` | 2.40 | sheets, waking (Runway) |
| 7.19 | `push-whoosh` | 0.35 | punch-in |
| 8.83 | `impact-bass-1` | 0.24 | riser into the brand drop (peaks 10.78) |
| 9.88 | `pencil-sketch` | 0.40 | red scribble |
| 10.67 | `brand-twinkle` | 0.45 | wordmark |
| 12.31 / 12.33 | `shimmer` / `pop` | 0.85 / 0.30 | DeepSleep® lockup / ring burst |
| 14.00 | `dive-whoosh` | 0.42 | zoom through into the night |
| 15.76 | `push-whoosh` | 0.30 | vertical whip |
| 16.99 | `charge-ticks` | 0.55 | five battery segments |
| 17.95 | `swoosh-air` | 0.35 | spin |
| 18.42 | `pulse` | 0.40 | circulation (Runway) |
| 20.95 | `light-shimmer` | 0.14 | hypnogram |
| 22.40 | `swoosh-air` | 0.30 | cloud rise |
| 25.19 | `push-whoosh` | 0.30 | dissolve to the stack |
| 26.12 | `swoosh-air` | 0.40 | cloud drift |
| 27.00 | `click-soft` | 0.35 | slot roll |
| 27.15 | `iris-whoosh` | 0.35 | fly-through into the end card |
| 28.06 / 29.25 | `brand-twinkle` / `pop` | 0.40 / 0.40 | end-card wordmark / SHOP NOW |

**Music:** an original instrumental generated for the ad (96 BPM, hushed nocturnal intro, drop at
10.12 s). Delayed 0.63 s so the drop lands on "Baller", spliced bar to bar (22.62 → 30.12 s) so the
fuller section carries the payoff from 23.25 s, faded over the end card; gain 0.20 under the VO.

**Mix:** −15.7 LUFS integrated, −1.5 dBTP (AAC), checked before each render with `tools/mix_preview.py`.
