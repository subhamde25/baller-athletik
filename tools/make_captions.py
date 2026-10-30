"""Build film/compositions/captions.html from the VO word timings.

python -I tools/make_captions.py   (run from baller-athletik/)

Each group = small Inter line(s) + one Playfair italic hero word, landing on the spoken words.
Edit GROUPS to retime, restyle or move a caption; word indices refer to assets/transcript-words.json.
"""
import json, html

VO_OFFSET = 0.25          # vo.wav starts here on the film timeline
WORDS = json.load(open("film/assets/transcript-words.json"))
INK, BLUE, WHITE, NAVY = "#111111", "#3e8ede", "#ffffff", "#0e2a47"

# start/end in film seconds; lines: ("s"|"h", [word indices]); colours: small, hero
GROUPS = [
    dict(id="g1", start=0.0, end=2.23, top=330, small=INK, hero="#1d5ea8", instant=True,
         lines=[("s", [0, 1, 2, 3, 4, 5]), ("h", [6])]),
    dict(id="g2", start=2.23, end=3.15, top=720, small=INK, hero=INK, hero_size=300, punch=True,
         lines=[("h", [7])]),
    dict(id="g3", start=3.15, end=5.95, top=300, small=INK, hero=BLUE,
         lines=[("s", [8, 9, 10, 11, 12, 13]), ("h", [14]), ("s", [15, 16, 17])]),
    dict(id="g4", start=5.95, end=7.25, top=780, small=WHITE, hero=WHITE,
         lines=[("s", [18, 19]), ("h", [20])]),
    dict(id="g5", start=7.25, end=8.5, top=780, small=WHITE, hero=WHITE,
         lines=[("s", [21, 22]), ("h", [23])]),
    dict(id="g6", start=8.5, end=10.55, top=780, small=WHITE, hero=WHITE,
         lines=[("s", [24, 25, 26, 27, 28]), ("h", [29])]),
    dict(id="g7", start=11.45, end=12.55, top=440, small=INK, hero=INK,
         lines=[("s", [32, 33, 34, 35])]),
    dict(id="g9", start=14.2, end=15.83, top=330, small=WHITE, hero=WHITE,
         lines=[("s", [38, 39, 40, 41, 42]), ("h", [43])]),
    dict(id="g10", start=15.83, end=16.83, top=300, small=INK, hero=BLUE, scrim="light",
         lines=[("s", [44]), ("h", [45])]),
    dict(id="g11", start=16.83, end=18.3, top=300, small=INK, hero=BLUE, scrim="light",
         lines=[("s", [46, 47, 48]), ("h", [49])]),
    dict(id="g12", start=18.42, end=19.95, top=760, small=WHITE, hero=WHITE,
         lines=[("s", [50, 51, 52]), ("h", [53])]),
    dict(id="g13", start=19.95, end=20.85, top=330, small=WHITE, hero=WHITE,
         lines=[("s", [54]), ("h", [55])]),
    dict(id="g14", start=20.85, end=22.75, top=330, small=WHITE, hero=WHITE,
         lines=[("s", [56, 57, 58, 59, 60, 61, 62]), ("h", [63])]),
    dict(id="g15", start=22.88, end=25.2, top=300, small=INK, hero=BLUE,
         lines=[("s", [64, 65, 66, 67, 68, 69]), ("h", [70])]),
    # "Upgrade your" holds while the hero rolls sleepwear. -> recovery. (shot changes at 26.6)
    dict(id="g16", start=25.25, end=27.95, top=300, small=INK, hero=NAVY, small_to=(WHITE, 26.8),
         lines=[("s", [71, 72]), ("r", [[73], [76]], [NAVY, WHITE])]),
]

def t(i):
    return round(WORDS[i]["start"] + VO_OFFSET, 3)

def hero_size(text, cap=186):
    # Playfair Display Italic 700 averages ~0.53 em per glyph; keep inside 940 px
    return int(min(cap, 940 / (0.53 * max(len(text), 1))))

def shadow(col):
    return "0 4px 26px rgb(0 0 0 / 38%)" if col == WHITE else "0 2px 18px rgb(255 255 255 / 55%)"

css, body, js = [], [], []
for g in GROUPS:
    gid = g["id"]
    body.append(f'    <div class="grp" id="cap-{gid}" style="top: {g["top"]}px">')
    if g.get("scrim"):
        body.append(f'      <div class="scrim {g["scrim"]}"></div>')
    for li, (kind, idxs, *_) in enumerate(g["lines"]):
        if kind == "s":
            spans = " ".join(
                f'<span class="w" id="cap-{gid}-w{i}">{html.escape(WORDS[i]["text"])}</span>' for i in idxs)
            body.append(f'      <div class="ln sm" style="color: {g["small"]}; text-shadow: {shadow(g["small"])}">{spans}</div>')
            for i in idxs:
                at = g["start"] if g.get("instant") else max(g["start"], t(i) - 0.04)
                if g.get("instant"):
                    continue  # on screen from frame 0 (thumbnail + hook)
                js.append(f'    tl.fromTo("#cap-{gid}-w{i}", {{ opacity: 0, filter: "blur(8px)" }}, '
                          f'{{ opacity: 1, filter: "blur(0px)", duration: 0.14, ease: "power2.out" }}, {at});')
        elif kind == "r":
            # slot roll: each option rolls up out of a clipped line as the next is spoken
            opts, cols = idxs, g["lines"][li][2]
            texts = [" ".join(WORDS[i]["text"] for i in o) for o in opts]
            size = min(hero_size(tx) for tx in texts)
            spans = "".join(f'<span class="w rw" id="cap-{gid}-r{k}" style="color: {c}; text-shadow: {shadow(c)}">{html.escape(tx)}</span>'
                            for k, (tx, c) in enumerate(zip(texts, cols)))
            body.append(f'      <div class="ln hero roll" style="font-size: {size}px; height: {round(size * 1.02)}px">{spans}</div>')
            at0 = max(g["start"], t(opts[0][0]) - 0.05)
            js.append(f'    tl.fromTo("#cap-{gid}-r0", {{ opacity: 0, scale: 1.18, filter: "blur(14px)" }}, '
                      f'{{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.32, ease: "expo.out" }}, {at0});')
            for k in range(1, len(opts)):
                T = round(t(opts[k][0]) - 0.14, 3)
                js.append(f'    tl.to("#cap-{gid}-r{k-1}", {{ yPercent: -110, filter: "blur(8px)", duration: 0.22, ease: "power3.in" }}, {T});')
                js.append(f'    tl.fromTo("#cap-{gid}-r{k}", {{ yPercent: 110, filter: "blur(8px)" }}, '
                          f'{{ yPercent: 0, filter: "blur(0px)", duration: 0.34, ease: "expo.out" }}, {round(T + 0.1, 3)});')
        else:
            text = " ".join(WORDS[i]["text"] for i in idxs)
            size = g.get("hero_size") or hero_size(text)
            body.append(f'      <div class="ln hero" style="font-size: {size}px; color: {g["hero"]}; text-shadow: {shadow(g["hero"])}">'
                        f'<span class="w" id="cap-{gid}-h">{html.escape(text)}</span></div>')
            at = max(g["start"], t(idxs[0]) - 0.05)
            s0 = 1.45 if g.get("punch") else 1.18
            js.append(f'    tl.fromTo("#cap-{gid}-h", {{ opacity: 0, scale: {s0}, filter: "blur(14px)" }}, '
                      f'{{ opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.32, ease: "expo.out" }}, {at});')
    body.append("    </div>")
    if g.get("small_to"):
        col, at = g["small_to"]
        js.append(f'    tl.to("#cap-{gid} .sm", {{ color: "{col}", textShadow: "{shadow(col)}", duration: 0.14, ease: "none" }}, {at});')
        js.append(f'    tl.to("#cap-{gid} .rw", {{ color: "{col}", textShadow: "{shadow(col)}", duration: 0.14, ease: "none" }}, {at});')
    js.append(f'    tl.set("#cap-{gid}", {{ opacity: 1, visibility: "visible" }}, {g["start"]});')
    js.append(f'    tl.to("#cap-{gid}", {{ opacity: 0, filter: "blur(10px)", duration: 0.16, ease: "power3.in" }}, {round(g["end"] - 0.16, 3)});')
    js.append(f'    tl.set("#cap-{gid}", {{ opacity: 0, visibility: "hidden" }}, {g["end"]});')

doc = f"""<template>
  <style>
    #root {{
      position: absolute;
      inset: 0;
      overflow: visible;
      pointer-events: none;
    }}
    #root .grp {{
      position: absolute;
      left: 0;
      width: 1080px;
      padding: 0 64px;
      text-align: center;
      opacity: 0;
      visibility: hidden;
      overflow: visible;
    }}
    #root .ln {{
      position: relative;
      display: block;
      white-space: nowrap;
    }}
    #root .sm {{
      font-family: "Inter", sans-serif;
      font-weight: 600;
      font-size: 50px;
      line-height: 1.18;
      letter-spacing: -0.01em;
    }}
    #root .hero {{
      font-family: "Playfair Display", serif;
      font-style: italic;
      font-weight: 700;
      line-height: 1.02;
      letter-spacing: -0.02em;
      margin: 2px 0 6px;
    }}
    #root .scrim {{
      position: absolute;
      left: 40px;
      right: 40px;
      top: -70px;
      bottom: -70px;
    }}
    #root .scrim.light {{
      background: radial-gradient(ellipse 50% 50% at 50% 50%, rgb(255 255 255 / 78%) 0%, rgb(255 255 255 / 45%) 55%, transparent 100%);
    }}
    #root .w {{
      display: inline-block;
    }}
    #root .roll {{
      clip-path: inset(-4% -40% -14% -40%);
    }}
    #root .rw {{
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      display: block;
      text-align: center;
    }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{chr(10).join(body)}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
    window.__timelines["captions"] = tl;
  </script>
</template>
"""
open("film/compositions/captions.html", "w", encoding="utf-8").write(doc)
print(len(GROUPS), "groups")
