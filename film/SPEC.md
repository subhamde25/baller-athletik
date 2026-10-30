# Baller Athletik — DeepSleep® Meta ad (Adbuffs test)

GOAL:    A tired viewer recognises themselves in the first 10 s, then sees Baller Athletik's DeepSleep® sleepwear as the fix and taps Shop Now.
OUTPUT:  HyperFrames, 1080 x 1920 (9:16 Meta Reels/Stories), 30 fps, MP4 H.264 + AAC.
TIME:    32.0 s x 30 = 960 frames. Music 96 BPM (18.75 frames/beat), bar = 2.5 s. Music drop on "Baller" at 10.75 s.
SAFE:    Meta 9:16: every word between y 270 and y 1250 (top 14 %, bottom 35 % kept clear of text), 64 px side margins.

LOOK (from the two Adbuffs reference ads):
  Two worlds. PROBLEM (0–10.75): real stock footage graded cool and grey — temp -0.18, sat -0.35, contrast +0.12,
  blue shadows (hue 210, 0.10), vignette 0.22, grain 0.06. BRAND (10.75–32): warm daylight — temp +0.08,
  vibrance +0.12, exposure +0.04, warm highlights (hue 38, 0.05), grain 0.04. NIGHT shots (deep sleep): cool
  contrast, shadows hue 220.
  Type: small line Inter 600, 50 px, tracking -1 %; hero word Playfair Display Italic 700, 132–190 px, tracking -2 %.
  Accent: sky blue #3E8EDE on light frames, white on dark/photo frames. Ink #111. Ground for type cards #F4F2EE.
  Brand marks: BALLER|ATHLETIK wordmark (Task 18.psd, upscaled), DeepSleep® Technology lockup (Task 18.psd).
  Text over photos gets a soft 0 6px 30px rgba(0,0,0,.35) shadow, never a box.

OBJECTS: alarm clock at 6:00 (hours), real people waking/sitting tired, the product (tees, shorts, sets),
  clouds (sleep), a battery (energy), blood vessels (circulation), a hypnogram (deep sleep longer).

MOTION:  arrivals expo.out / power4.out; camera power2.inOut; exits power3.in, 40 % shorter than entrances.
  Small line: per word blur 8→0 + opacity, 0.14 s, 0.07 s apart. Hero word: scale 1.18→1, blur 14→0, 0.32 s expo.out,
  lands on its spoken word. Group exit: blur 0→10 + fade 0.16 s. Stills: one camera move each (push 1.0→1.08 or
  pull 1.2→1.04). Hero moves 1 per shot.

SHOTS (VO starts 0.25 s; times = film seconds):
  01 0.00–2.23  hook_alarm (hand reaches for clock), PROBLEM grade, push 1.0→1.1. "Think sleep is just about the" on
                screen at frame 0; "hours?" lands 1.31. SFX alarm ring 0.0.
  02 2.23–3.15  type card #F4F2EE, "Nope." Playfair 300 px ink, punches 1.25→1 with blur. Hard cut. SFX impact.
  03 3.15–5.95  clouds_man still, pull 1.22→1.04 (floating up). "It's about how well your body / recovers / while you rest."
                Enter: blur swap (20→0 px, 0.35 s). SFX swoosh-air.
  04 5.95–7.25  wake_a (night, man rubs face), PROBLEM grade. "Waking up / tired?" Enter: dip cut. SFX rustle.
  05 7.25–8.50  wake_b (hunched), punch-in cut. "Muscles still / sore?"
  06 8.50–10.75 wake_c (slumped on bed edge), slow push. "Your sleepwear might be the / problem." Riser 9.55→10.75.
     10.45–11.3 TRANSITION: warm light leak + white flash (wake-up) into BRAND world on the music drop.
  07 10.75–12.60 brand_model (4K, model in grey tee on white), scale 1.3. Wordmark wipes in at 10.85, 880 px wide.
                "sleepwear is made with". SFX impact + twinkle.
  08 12.60–14.10 waistband (4K close-up), DeepSleep® Technology lockup reveals 12.69 (mask wipe + blur). SFX shimmer.
                Exit: zoom-through into the black shorts (1→2.4, power3.in, 0.35 s) → night.
  09 14.10–15.83 deep_night (man on night clouds), sink: y -60→0, scale 1.15→1.05. "designed to help you / sleep deeper,"
                SFX dive-whoosh.
  10 15.83–16.83 stretch_mint (overhead), punch 1.14→1.0 expo.out. "recover / faster,"
  11 16.83–18.37 stretch (man at window), BRAND grade. Battery outline fills 18 %→100 % (16.95–17.9). "and wake up / energized."
                SFX charge.
  12 18.37–19.95 drawn vessel macro: deep red field, 3 depth layers of branching vessels, flowing cells; slow push.
                "It helps improve / circulation," SFX pulse.
  13 19.95–20.85 muscle_sleep still, push on the arm. "relax / muscles,"
  14 20.85–22.83 longer_dark still + hypnogram: Awake/Light/Deep line draws, Deep plateau highlighted blue.
                "and keep your body in deep sleep / longer,"
  15 22.83–23.87 cloud_bed (woman stretching on a bed in the sky). "so you wake up feeling your"
  16 23.87–25.25 best_stretch, "best." lands at the cut (music full section from 23.25).
  17 25.25–26.60 stack_sky, "Upgrade your / sleepwear."
  18 26.60–28.00 fly_pink, "Upgrade your / recovery."
  19 28.00–32.00 END CARD: pink shorts on sky, wordmark, "Try Baller Athletik today.", SHOP NOW button (rect, r 6).
                SFX impact at 28.1. Holds 3.4 s.

SOUND:  VO (supplied ElevenLabs read + Fish clone of the same voice for "Try Baller Athletik today.") at -16 LUFS.
  Original music bed (96 BPM, hushed until the brand drop, fuller from 23.25) at 0.16 under VO.
  Effects only on visible causes; whooshes rotated (swoosh-air / dive / push / iris). Mix -14 LUFS, TP <= -1 dBTP.

BANNED: dark void with floating elements; neon/glow orbs; everything centred-and-fading; text moving while read;
  logo docked in a corner; the same whoosh on every cut; captions under y 1250; AI sparkle marks in frame.

QA: 0.0 (hook readable), 2.5 (Nope), 4.6 (recovers), 10.6–11.0 (flash into brand), 12.9 (DeepSleep), 17.5 (battery),
  19.0 (vessels), 22.0 (hypnogram), 26.0, 29.5 (end card, everything above y 1250).

## v3 transitions (from a frame-by-frame study of the two reference ads)
3.0 dream cloud (cloud-shaped mask grows from the Nope card, thought puffs) · 5.95 cloud fall (band wipe up) ·
12.6 ring burst + circle iris · 14.0 night cloud fly-through · 15.73 vertical whip (SVG y-blur) · 16.83 warm film burn ·
18.37 spin + zoom blur · 19.95 focus pull · 22.83 cloud rise (band wipe down) · 23.87 white flash · 25.25 blur dissolve ·
26.6 sideways cloud drift · 27.55 bright cloud fly-through. Foreground cloud layers drift on every sky shot and the end card.
Cloud cutouts: Runway renders on black → keyed by tools/key_clouds.py / make_band.py into film/assets/img/clouds/.
