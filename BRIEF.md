# Brief

**Client test:** Adbuffs, design round for a motion designer / video editor (received 2026-10-23).

**Task:** create a Meta video ad for **Baller Athletik**, a brand that mostly sells sleepwear. It
should look premium and match the standard of the two reference ads.

**Size:** 1080×1920 px.

**Copy (fixed):**

> Think sleep is just about the hours?
> Nope. It's about how well your body recovers while you rest.
> Waking up tired? Muscles still sore? Your sleepwear might be the problem.
> Baller Athletik sleepwear is made with DeepSleep® Technology, designed to help you sleep deeper,
> recover faster, and wake up energized.
> It helps improve circulation, relax muscles, and keep your body in deep sleep longer—so you wake
> up feeling your best.
> Upgrade your sleepwear. Upgrade your recovery. Try Baller Athletik today.

**Note from the brief:** "We do not grant permission to use the test project in your portfolio,
doing this can bring in legal action from Business owner and Adbuffs."

## Supplied (public Google Drive folders)

| Folder | Drive id | What's in it |
|---|---|---|
| Video reference | `1fN0ZeSYY9TNoTbN-bHh9kEnvizVasyKl` | `Task 19 (3).mp4` (31.7 s, 25 fps) and `Task 20.mp4` (32.5 s, 30 fps), both 1080×1920 Baller Athletik ads |
| Video ads | `1S503zoBVQCINZjelOFdXPA8OeNX0uOef` | 38 creator UGC sleep ads (Men Sleep / Women Sleep), 9:16 and 1:1 |
| Image Dump | `16RWJGg0myk6bLTfJ_GuDbr-Q873Rm2-s` | ~520 images: product shots, editorial, AI-generated ads, PSDs |
| Additional Assets | `1vqsmq1k3hXAuyv28thKzjxGW8WVXJky-` | 3 4K product clips, 4 HD stock clips, `Task 18.psd`, the ElevenLabs male voice-over |

The brief says the folders hold "logo, voice-over, and other assets". There is no standalone logo
file: the BALLER|ATHLETIK wordmark and the DeepSleep® lockup were extracted from `Task 18.psd`
(`tools/extract_brand.py`). "Team Logos" are sports-team partners; `fix logo.png` is a photo.

The supplied voice-over (27.6 s) reads the copy word for word but stops at "Upgrade your recovery."
The closing line was voiced with a private Fish Audio clone of the same voice.

## References

Both reference ads were studied frame by frame (`tools/trans_sheet.py`, 10 frames 67 ms apart around
every cut). What they do and how this edit uses it is in [`BREAKDOWN.md`](BREAKDOWN.md#reference-study).
