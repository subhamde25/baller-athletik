#!/bin/sh
# Trim + crop source footage to 1080x1920/30fps shots in film/assets/video.
A="raw/Additional Assets"; O="film/assets/video"
ALARM="$A/sleepy-man-turns-off-the-alarm-in-the-early-morning-while-continuing-to-sleep-SBV-346653066-HD.mp4"
WAKE="$A/man-waking-up-getting-out-of-bed-in-the-middle-of-the-night-ealy-wake-up-in-the-mor-SBV-348898194-HD.mp4"
STRETCH="$A/man-in-the-morning-raising-his-hands-and-stretching-media-young-man-looking-through-SBV-348647413-HD.mp4"
cut() { # src start dur cropx out  (cropx = left edge of a 608px window in 1920x1080; "v" = already vertical)
  if [ "$4" = v ]; then vf="scale=1080:1920:flags=lanczos"; else vf="crop=608:1080:$4:0,scale=1080:1920:flags=lanczos,unsharp=5:5:0.6"; fi
  ffmpeg -v error -y -ss "$2" -t "$3" -i "$1" -an -vf "$vf,fps=30,format=yuv420p" -c:v libx264 -crf 16 -preset slow -movflags +faststart "$O/$5.mp4"
  echo "$5 $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$O/$5.mp4")"
}
cut "$ALARM" 1.2 3.2 960 hook_alarm
cut "$WAKE" 5.4 2.2 1140 wake_a
cut "$WAKE" 7.6 2.2 780 wake_b
cut "$WAKE" 12.4 3.0 1312 wake_c
cut "$STRETCH" 2.9 2.4 626 stretch
cut "$A/C3035_1.mp4" 9.4 3.0 v brand_model
cut "$A/C3040_1.mp4" 0.2 2.4 v waistband
cut "$A/C3037_1.mp4" 0.3 2.6 v sleeve
