# Photo (left) + schematic cutaway (right) comparison images for each dome.
# Cutaway geometry mirrors cutaway() in interactive_template.html.
import json, subprocess, io, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

PAPER, INK, SEPIA, RULE = '#efe6d2', '#2a2118', '#5b4a36', '#6b5942'
G = '/System/Library/Fonts/Supplemental/Georgia.ttf'
GI = '/System/Library/Fonts/Supplemental/Georgia Italic.ttf'
GB = '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'
RSVG = '/Users/soumya/mambaforge/bin/rsvg-convert'

def cutaway_svg(kind, col):
    hatch = (f'<pattern id="h" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
             f'<line x1="0" y1="0" x2="0" y2="5" stroke="{RULE}" stroke-width=".8" opacity=".45"/></pattern>')
    def wall(x0, x1, top):
        return (f'<rect x="{x0}" y="{top}" width="12" height="{200-top}" fill="url(#h)" stroke="{INK}" stroke-width="1"/>'
                f'<rect x="{x1-12}" y="{top}" width="12" height="{200-top}" fill="url(#h)" stroke="{INK}" stroke-width="1"/>')
    lab = lambda x, y, t, a='start': f'<text x="{x}" y="{y}" font-family="Georgia" font-size="8.5" fill="{SEPIA}" text-anchor="{a}" font-style="italic">{t}</text>'
    outer = lambda d: f'<path d="{d}" fill="none" stroke="{col}" stroke-width="5" stroke-linejoin="round"/>'
    inner = lambda d: f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="3"/>'
    gap = lambda d: f'<path d="{d}" fill="{col}" opacity=".13"/>'
    pier = lambda x, y, h: f'<rect x="{x}" y="{y}" width="10" height="{h}" fill="url(#h)" stroke="{INK}"/>'
    g = ''
    if kind == 'lodi':
        g += gap('M48,120 A52,52 0 0 1 152,120 L146,120 A46,44 0 0 0 54,120 Z')
        g += wall(42, 158, 120) + outer('M48,120 A52,52 0 0 1 152,120') + inner('M54,120 A46,44 0 0 1 146,120')
        g += f'<line x1="100" y1="68" x2="100" y2="58" stroke="{INK}" stroke-width="1.5"/>'
        g += lab(156, 80, 'outer shell') + lab(100, 110, 'inner shell', 'middle') + lab(100, 160, 'tomb chamber', 'middle')
    elif kind == 'humayun':
        g += gap('M62,96 C50,60 78,30 100,18 C122,30 150,60 138,96 Z')
        g += wall(30, 170, 132) + pier(58, 96, 36) + pier(132, 96, 36)
        g += outer('M62,96 C50,60 78,30 100,18 C122,30 150,60 138,96') + inner('M68,132 A32,28 0 0 1 132,132') + f'<line x1="30" y1="132" x2="58" y2="132" stroke="{INK}" stroke-width="1.4"/><line x1="142" y1="132" x2="170" y2="132" stroke="{INK}" stroke-width="1.4"/>'
        g += f'<line x1="100" y1="18" x2="100" y2="6" stroke="{INK}" stroke-width="1.5"/>'
        g += f'<rect x="59.5" y="101" width="7" height="6" fill="{PAPER}" stroke="{INK}" stroke-width=".9"/>' + f'<path d="M133.5,132 V123 Q137,118 140.5,123 V132 Z" fill="{PAPER}" stroke="{INK}" stroke-width=".9"/>'   # documented openings (AKTC; Lowry 1987)
        g += lab(146, 46, 'tall outer shell') + lab(100, 78, 'large gap', 'middle') + lab(100, 127, 'inner dome', 'middle') + lab(100, 170, 'burial hall', 'middle')
        g += lab(54, 99, 'small access', 'end') + lab(54, 108, 'opening', 'end') + lab(146, 116, 'doorway from') + lab(146, 125, 'roof terrace')
    elif kind == 'rb':
        g += gap('M55,118 A45,44 0 0 1 145,118 Z')
        g += wall(30, 170, 140) + pier(50, 118, 22) + pier(140, 118, 22)
        g += outer('M55,118 A45,44 0 0 1 145,118') + f'<rect x="96" y="68" width="8" height="8" fill="{col}" stroke="{INK}"/>'
        g += inner('M60,140 A40,30 0 0 1 95,110.24') + inner('M105,110.24 A40,30 0 0 1 140,140') + lab(100, 106, 'oculus', 'middle') + f'<line x1="30" y1="140" x2="50" y2="140" stroke="{INK}" stroke-width="1.4"/><line x1="150" y1="140" x2="170" y2="140" stroke="{INK}" stroke-width="1.4"/>'
        g += lab(146, 82, 'copper-clad outer') + lab(100, 135, 'inner dome', 'middle') + lab(100, 175, 'Durbar Hall', 'middle')
    else:  # florence
        g += gap('M40,120 Q46,50 100,26 Q154,50 160,120 L150,120 Q144,62 100,44 Q56,62 50,120 Z')
        g += wall(28, 172, 120)
        g += f'<path d="M40,120 Q46,50 100,26 Q154,50 160,120" fill="none" stroke="{col}" stroke-width="2.5"/>' + f'<path d="M50,120 Q56,62 100,44 Q144,62 150,120" fill="none" stroke="{INK}" stroke-width="7"/>'
        g += f'<rect x="94" y="10" width="12" height="16" fill="{col}" stroke="{INK}"/>'
        g += f'<path d="M153.9,111.1 L153.9,102.6 L152.4,102.6 L152.4,94.5 L150.5,94.5 L150.5,86.9 L148.1,86.9 L148.1,79.8 L145.2,79.8 L145.2,73.0 L142.0,73.0 L142.0,66.8 L138.2,66.8 L138.2,60.9 L134.1,60.9 L134.1,55.5 L129.5,55.5" fill="none" stroke="{SEPIA}" stroke-width="1.1"/>'   # the climb between the shells
        g += lab(160, 66, 'thin outer shell') + lab(162, 100, 'stairs between') + lab(162, 110, 'the shells') + lab(100, 96, 'thick inner shell', 'middle') + lab(100, 170, 'octagonal drum', 'middle')
    g += f'<line x1="10" y1="200" x2="190" y2="200" stroke="{INK}" stroke-width="1.2"/>'
    # wider viewBox so right-hand labels are never clipped
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 210" width="230" height="210"><defs>{hatch}</defs>{g}</svg>'

def render_svg(svg, width):
    png = subprocess.run([RSVG, '-w', str(width), '-b', PAPER], input=svg.encode(), capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(png)).convert('RGB')

def wrap(draw, text, font, width):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=font) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]

DOMES = {
 'lodi': dict(title='Sikandar Lodi’s tomb, Lodi Gardens, Delhi', date='1517–18', col='#7d9a3c',
              line='Persian tradition, early in India. Often cited as India’s first double dome; some historians call it only a first step.'),
 'humayun': dict(title='Humayun’s Tomb, Delhi', date='1565–72', col='#c49a1e',
              line='Persian–Timurid, mature. A tall outer shell for the skyline over a low inner dome that keeps the hall in proportion. Unlike Florence, no stair runs between the shells: conservators reached the cavity through a 0.8 × 0.6 m opening and scaffolding (AKTC).'),
 'rb': dict(title='Rashtrapati Bhavan, New Delhi', date='1912–29', col='#7a2e4f',
              line='European classical, Sanchi-shaped. A copper-clad outer dome over a lower inner dome, about 22 m across with a central oculus, above Durbar Hall.'),
 'florence': dict(title='Florence Cathedral (Santa Maria del Fiore)', date='1420–36', col='#6b5942',
              line='Italian Renaissance. The double shell was already in the 1367 design; Brunelleschi built it without timber centring. The thick inner shell carries the load; visitors climb 463 steps between the shells.'),
}
credits = json.load(open('photo_credits.json'))
H = 2400                                # photo height in output
os.makedirs('../blog/domes', exist_ok=True)
for k, d in DOMES.items():
    photo = ImageOps.exif_transpose(Image.open(f'../photos_dl/{k}.jpg')).convert('RGB')
    pw = round(photo.width * H / photo.height); photo = photo.resize((pw, H), Image.LANCZOS)
    RW = 1900                           # right panel width
    pad = 80
    W = pw + RW
    head, foot = 230, 260
    canvas = Image.new('RGB', (W, H + head + foot), PAPER)
    canvas.paste(photo, (0, head))
    dr = ImageDraw.Draw(canvas)
    # header across the top
    dr.text((pad, 50), d['title'], font=ImageFont.truetype(G, 84), fill=INK)
    dr.text((pad, 150), d['date'], font=ImageFont.truetype(GB, 52), fill=d['col'])
    # right panel: cutaway + caption
    cw = RW - 2 * pad
    cut = render_svg(cutaway_svg(k, d['col']), cw)
    canvas.paste(cut, (pw + pad, head + 140))
    dr.text((pw + pad, head + 50), 'Outer and inner shells, in section', font=ImageFont.truetype(G, 54), fill=INK)
    y = head + 140 + cut.height + 40
    f_body = ImageFont.truetype(G, 44)
    for ln in wrap(dr, d['line'], f_body, cw):
        dr.text((pw + pad, y), ln, font=f_body, fill=INK); y += 60
    y += 20
    dr.rectangle([pw + pad, y + 8, pw + pad + 60, y + 22], fill=d['col']); dr.text((pw + pad + 80, y - 6), 'outer shell', font=ImageFont.truetype(GI, 38), fill=SEPIA)
    dr.rectangle([pw + pad + 380, y + 10, pw + pad + 440, y + 20], fill=INK); dr.text((pw + pad + 460, y - 6), 'inner shell', font=ImageFont.truetype(GI, 38), fill=SEPIA)
    y += 70
    dr.text((pw + pad, y), 'Schematic, not to scale.', font=ImageFont.truetype(GI, 38), fill=SEPIA)
    # credits
    c = credits[k]
    f_cr = ImageFont.truetype(GI, 34)
    y = head + H + 40
    lines = [f'Photo: {c["artist"]}, “{c["file"]}”, Wikimedia Commons, {c["lic"]}' + (f' ({c["lic_url"]})' if c['lic_url'] else '') + '.',
             'Cutaway: schematic drawing for “How to Time Travel in Delhi”.']
    if 'SA' in c['lic']:
        lines.append(f'This combined image is shared under {c["lic"]}.')
    for t in lines:
        for ln in wrap(dr, t, f_cr, W - 2 * pad):
            dr.text((pad, y), ln, font=f_cr, fill=SEPIA); y += 48
    out = f'../blog/domes/{k}_photo_vs_cutaway.jpg'
    canvas.save(out, quality=90, optimize=True, subsampling=0)
    print(out, canvas.size)
