#!/usr/bin/env python3
"""Build animation.html: bg2 icons with click-pop entrance + idle float, transparent bg."""
from pathlib import Path

ROOT = Path(__file__).parent
bg2 = (ROOT / "bg2.svg").read_text().splitlines(keepends=False)

# 1-indexed line ranges in the new bg2.svg (12 floating elements + 3 static cards).
FLOATING = [
    {"start": 2,   "end": 10,  "cx":  97, "cy": 204},   # filter0: white pill, green flag
    {"start": 11,  "end": 27,  "cx": 290, "cy": 219},   # filter1: orange reddit
    {"start": 28,  "end": 38,  "cx": 130, "cy":  56},   # filter2: large black tiktok
    {"start": 39,  "end": 43,  "cx": 432, "cy":  91},   # filter3: orange MS-like
    {"start": 44,  "end": 52,  "cx": 215, "cy": 145},   # filter4: large white red note
    {"start": 53,  "end": 75,  "cx": 331, "cy":  55},   # filter5: white pinterest
    {"start": 76,  "end": 82,  "cx": 504, "cy": 124},   # filter6: white MS color
    {"start": 83,  "end": 92,  "cx": 388, "cy": 180},   # filter7: small white multi
    {"start": 93,  "end": 100, "cx":  39, "cy": 145},   # standalone white square
    {"start": 101, "end": 102, "cx": 228, "cy":  18},   # Facebook F badge (blue circle + white F)
    {"start": 103, "end": 148, "cx": 493, "cy":  33},   # filter8: Gemini-like sparkle with glow
    {"start": 149, "end": 157, "cx": 503, "cy": 197},   # filter20: white pill far-right
]

CX, CY = 295, 261

# Sanity-check: confirm starts look like opening tags so we know the line offsets are right.
for item in FLOATING:
    line = bg2[item["start"] - 1].lstrip()
    assert line.startswith("<g ") or line.startswith("<rect") or line.startswith("<path"), (
        f"unexpected start line {item['start']}: {line[:80]}"
    )

inject_class_on = {}
wrap_open_at = {}
wrap_close_at = {}

for i, item in enumerate(FLOATING):
    s, e = item["start"], item["end"]
    if bg2[s - 1].lstrip().startswith("<g "):
        inject_class_on[s] = i
    else:
        wrap_open_at[s] = i
        wrap_close_at[e] = i


def style_for(i):
    item = FLOATING[i]
    cx, cy = item["cx"], item["cy"]
    # entry transform start
    dx = (cx - CX) * 0.12         # gentle outward fan
    dy = 260 + (i % 4) * 50       # rise distance: bigger so the upward inertia reads more
    rot = ((i * 53) % 24) - 12    # -12..12 deg initial tilt
    delay = 0.05 + i * 0.09       # bigger stagger so eyes can track each pop
    bob_amp = 4 + (i % 3) * 1.5
    bob_dur = 3.6 + (i * 0.17) % 1.4
    bob_phase = -((i * 0.31) % bob_dur)
    return (
        f"--dx:{dx:.1f}px; --dy:{dy:.0f}px; --rot:{rot}deg; "
        f"--delay:{delay:.2f}s; --bob-amp:{bob_amp:.1f}px; "
        f"--bob-dur:{bob_dur:.2f}s; --bob-phase:{bob_phase:.2f}s;"
    )


out_lines = []
for idx, raw in enumerate(bg2, start=1):
    if idx in wrap_open_at:
        i = wrap_open_at[idx]
        out_lines.append(f'<g class="float-icon" style="{style_for(i)}">')
        prepend = FLOATING[i].get("prepend")
        if prepend:
            out_lines.append(prepend)

    if idx in inject_class_on:
        i = inject_class_on[idx]
        out_lines.append(raw.replace(
            "<g ",
            f'<g class="float-icon" style="{style_for(i)}" ',
            1,
        ))
    else:
        # Always output the raw line unless it was modified by inject_class_on
        out_lines.append(raw)

    if idx in wrap_close_at:
        out_lines.append("</g>")

svg_body = "\n".join(out_lines)

# Build click ripple overlay — three concentric expanding rings at the canvas center bottom,
# fired at t=0..0.5s, fading out before icons land.
# Position at the bottom center where the icons "burst from".
RIPPLE_X, RIPPLE_Y = 295, 360

ripple_svg = f"""
<g class="click-ripple" transform="translate({RIPPLE_X} {RIPPLE_Y})">
  <circle r="6" class="ripple-dot" />
  <circle r="6" class="ripple-ring ring-1" fill="none" stroke="#1250FC" stroke-width="2" />
  <circle r="6" class="ripple-ring ring-2" fill="none" stroke="#1250FC" stroke-width="2" />
  <circle r="6" class="ripple-ring ring-3" fill="none" stroke="#1250FC" stroke-width="2" />
</g>
"""

# Inject ripple right after the opening <svg ...> tag.
svg_body = svg_body.replace(
    '<svg width="590" height="522"',
    '<svg width="590" height="522"',
    1,
)
# Find first newline after <svg ...> and insert ripple there.
svg_body = svg_body.replace("\n", ripple_svg + "\n", 1)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Floating icons animation</title>
<style>
  :root {{ color-scheme: light; }}
  html, body {{
    margin: 0; padding: 0; height: 100%;
    background: transparent;
  }}
  body {{
    display: flex; align-items: center; justify-content: center;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }}
  .stage {{
    position: relative;
    width: 590px; height: 522px;
    overflow: visible;
    background: transparent;
  }}
  .stage svg {{ display: block; width: 100%; height: 100%; overflow: visible; }}
  .replay {{
    position: absolute; top: 12px; right: 12px;
    padding: 8px 14px; border-radius: 999px; border: 1px solid #d4dadd;
    background: white; font-size: 13px; cursor: pointer;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06); z-index: 2;
  }}
  .replay:hover {{ background: #f8f9fa; }}

  /* Each icon: scale-pop entrance from below + idle bob.
     No overshoot — decelerating ease-out (easeOutExpo style) so the icon glides
     smoothly to its final position with a sense of inertia, but never reverses direction. */
  .float-icon {{
    transform-box: fill-box;
    transform-origin: center;
    will-change: transform, opacity;
    animation:
      icon-pop 1.5s cubic-bezier(0.16, 1, 0.3, 1) var(--delay) both,
      icon-fade 0.55s ease-out var(--delay) both,
      icon-bob var(--bob-dur) ease-in-out calc(var(--delay) + 1.5s + var(--bob-phase)) infinite;
  }}

  @keyframes icon-pop {{
    from {{ transform: translate(var(--dx), var(--dy)) rotate(var(--rot)) scale(0.2); }}
    to   {{ transform: translate(0, 0) rotate(0deg) scale(1); }}
  }}

  @keyframes icon-fade {{
    from {{ opacity: 0; }}
    to   {{ opacity: 1; }}
  }}

  @keyframes icon-bob {{
    0%, 100% {{ transform: translate(0, 0); }}
    50%      {{ transform: translate(0, calc(var(--bob-amp) * -1)); }}
  }}

  /* Click ripple: short tap burst at the start. */
  .click-ripple {{
    pointer-events: none;
  }}
  .ripple-dot {{
    fill: #1250FC;
    transform-origin: center;
    transform-box: fill-box;
    animation: dot-pop 0.45s ease-out 0s both;
  }}
  .ripple-ring {{
    transform-origin: center;
    transform-box: fill-box;
    opacity: 0;
  }}
  .ring-1 {{ animation: ring-expand 0.6s ease-out 0.05s both; }}
  .ring-2 {{ animation: ring-expand 0.6s ease-out 0.18s both; }}
  .ring-3 {{ animation: ring-expand 0.6s ease-out 0.31s both; }}

  @keyframes dot-pop {{
    0%   {{ transform: scale(0); opacity: 0; }}
    35%  {{ transform: scale(1.4); opacity: 1; }}
    65%  {{ transform: scale(1); opacity: 1; }}
    100% {{ transform: scale(0); opacity: 0; }}
  }}

  @keyframes ring-expand {{
    0%   {{ transform: scale(0.3); opacity: 0.85; }}
    100% {{ transform: scale(6); opacity: 0; }}
  }}

  @media (prefers-reduced-motion: reduce) {{
    .float-icon, .ripple-dot, .ripple-ring {{ animation: none; }}
  }}
</style>
</head>
<body>
  <div class="stage">
    <button class="replay" type="button" onclick="replay()">Replay</button>
{svg_body}
  </div>
<script>
  function replay() {{
    document.querySelectorAll('.float-icon, .ripple-dot, .ripple-ring').forEach(el => {{
      el.style.animation = 'none';
      void el.offsetWidth;
      el.style.animation = '';
    }});
  }}
</script>
</body>
</html>
"""

(ROOT / "animation.html").write_text(html)
print(f"Wrote animation.html ({len(html):,} bytes), floating icons: {len(FLOATING)}")
