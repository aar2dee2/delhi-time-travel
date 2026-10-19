# Blog images from the static map: full poster (4800 px PNG, 2400 px JPG) and a map-only crop
# with its own title and credits. Run from the project root after build.py has written the SVG.
import subprocess
from PIL import Image, ImageDraw, ImageFont

G = '/System/Library/Fonts/Supplemental/Georgia.ttf'
GI = '/System/Library/Fonts/Supplemental/Georgia Italic.ttf'
BG, INK, SEP = (239, 230, 210), (42, 33, 24), (91, 74, 54)

subprocess.run(['/Users/soumya/mambaforge/bin/rsvg-convert', '-z', '3', 'delhi_deep_time_map.svg',
                '-o', 'blog/delhi_time_travel_poster_4800px.png'], check=True)
im = Image.open('blog/delhi_time_travel_poster_4800px.png').convert('RGB')
im.resize((2400, round(im.height * 2400 / im.width)), Image.LANCZOS).save(
    'blog/delhi_time_travel_poster_2400px.jpg', quality=90, optimize=True)

S, pad = 3, 60
m = im.crop((24 * S, 104 * S, 656 * S, 1016 * S))          # map frame plus a small margin
W = m.width + 2 * pad
title, sub, small = ImageFont.truetype(G, 92), ImageFont.truetype(GI, 40), ImageFont.truetype(GI, 30)
credit = ['Numbers give founding order; colours give the century. Real driving and walking routes from OpenStreetMap routing (FOSSGIS OSRM).',
          'Positions: Wikipedia/OpenStreetMap coordinates. Road and river data © OpenStreetMap contributors (ODbL).']

def wrap(draw, text, font, width):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]

probe = ImageDraw.Draw(Image.new('RGB', (1, 1)))
lines = [l for c in credit for l in wrap(probe, c, small, W - 2 * pad)]
line_h, top = 44, 240
H = top + m.height + 30 + len(lines) * line_h + 40        # canvas sized to fit every credit line
out = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(out)
d.text((pad, 40), 'HOW TO TIME TRAVEL IN DELHI', font=title, fill=INK)
d.text((pad, 160), 'Fifteen monuments, a thousand years of capitals, all within about 13 km of Raisina Hill', font=sub, fill=SEP)
out.paste(m, (pad, top))
y = top + m.height + 30
for l in lines:
    d.text((pad, y), l, font=small, fill=SEP); y += line_h
out.save('blog/delhi_time_travel_map_only.png', optimize=True)
print('map only', out.size, 'last credit line ends at', y, 'of', H)
