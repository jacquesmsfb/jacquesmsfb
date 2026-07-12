"""Renders dragon.txt as a scalable SVG (one per color theme).

SVG (not PNG) so the art stays crisp at any zoom, and GitHub's own
img{max-width:100%} rule makes it scale down responsively on narrow/mobile
viewports -- something raw <pre> text can't do, since GitHub strips
custom CSS from README HTML. Two color variants + a <picture> element in
the README give automatic light/dark GitHub theme adaptation.
"""
import html

FONT_SIZE = 14
LINE_HEIGHT = 16
CHAR_WIDTH = FONT_SIZE * 0.6  # standard monospace advance-width ratio
FONT_STACK = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

with open("dragon.txt", "r") as f:
    lines = f.read().split("\n")
    while lines and lines[-1].strip() == "":
        lines.pop()

max_len = max(len(line) for line in lines)
width = round(max_len * CHAR_WIDTH) + 4
height = len(lines) * LINE_HEIGHT + 4


def build_svg(fill_color: str) -> str:
    text_lines = []
    for i, line in enumerate(lines):
        y = (i + 1) * LINE_HEIGHT
        escaped = html.escape(line)
        text_lines.append(
            f'<text x="0" y="{y}" xml:space="preserve">{escaped}</text>'
        )
    body = "\n    ".join(text_lines)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    text {{ font-family: {FONT_STACK}; font-size: {FONT_SIZE}px; fill: {fill_color}; }}
  </style>
  <g>
    {body}
  </g>
</svg>
'''


with open("dragon-light.svg", "w") as f:
    f.write(build_svg("#24292f"))  # dark charcoal, for GitHub's light theme

with open("dragon-dark.svg", "w") as f:
    f.write(build_svg("#e6edf3"))  # off-white, for GitHub's dark theme

print(f"Generated dragon-light.svg / dragon-dark.svg: {width}x{height}px viewBox, {len(lines)} lines")
