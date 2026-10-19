import json, math, sys
from icons import ICONS, INK, PAPER, ANCIENT

W, H = 1600, 1140
BG = '#efe6d2'
SEPIA = '#5b4a36'
RULE = '#6b5942'
ROUTE = '#8a2f1f'

S = {s['id']: s for s in json.load(open('sites.json'))}
R = json.load(open('routes.json'))
Y = json.load(open('yamuna.json'))
lat0, lon0 = S['rb']['lat'], S['rb']['lon']

# ---------- map frame & projection (local equirectangular, north up) ----------
K = 44                       # px per km
MX0, MY0, MX1, MY1 = 30, 110, 650, 1010
XMIN, YMIN = -4.6, -6.8
CX, CY = MX0 + (0 - XMIN) * K, MY0 + (0 - YMIN) * K

def proj(lat, lon):
    x = (lon - lon0) * math.cos(math.radians(lat0)) * 111.32
    y = -(lat - lat0) * 110.574
    return MX0 + (x - XMIN) * K, MY0 + (y - YMIN) * K

def hav(a, b):
    R_ = 6371.0088
    p1, p2 = math.radians(a['lat']), math.radians(b['lat'])
    dl = math.radians(b['lon'] - a['lon'])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_ * math.asin(math.sqrt(h))

# ---------- site catalogue (fact-checked) ----------
# n, id, name, built (label), start year for plotting, patron, century key
SITES = [
    (1, 'lalkot', 'Lal Kot', 'c.1060', 1060, 'Anangpal II Tomar; Qila Rai Pithora 12th c.', 11),
    (2, 'qutb', 'Qutb Minar', 'c.1199–1220', 1199, 'Aibak, then Iltutmish; Iron Pillar c.400 CE', 12),
    (3, 'siri', 'Siri', 'c.1303', 1303, 'Alauddin Khalji', 14),
    (4, 'tughlaq', 'Tughlaqabad', '1321–c.1325', 1321, 'Ghiyas-ud-din Tughlaq', 14),
    (5, 'jahan', 'Jahanpanah', 'c.1326–27', 1326, 'Muhammad bin Tughlaq (Bijay Mandal)', 14),
    (6, 'kotla', 'Feroz Shah Kotla', '1354', 1354, 'Firuz Shah Tughlaq; Ashokan Pillar 3rd c. BCE', 14),
    (7, 'lodi', 'Lodi Gardens', '1444–1518', 1444, 'Sayyid & Lodi sultans', 15),
    (8, 'purana', 'Purana Qila', '1533–c.1545', 1533, 'Humayun, then Sher Shah Suri', 16),
    (9, 'humayun', 'Humayun’s Tomb', '1565–72', 1565, 'Bega (Haji) Begum; Mirak Mirza Ghiyas', 16),
    (10, 'redfort', 'Red Fort', '1639–48', 1639, 'Shah Jahan', 17),
    (11, 'jama', 'Jama Masjid', '1650–56', 1650, 'Shah Jahan', 17),
    (12, 'jantar', 'Jantar Mantar', '1724', 1724, 'Jai Singh II of Amber', 18),
    (13, 'safdar', 'Safdarjung’s Tomb', 'c.1754', 1754, 'Shuja-ud-Daula, for his father', 18),
    (14, 'sisganj', 'Sis Ganj Sahib', '1783 · bldg 1930', 1783, 'Baghel Singh; marks the 1675 martyrdom', 18),
    (15, 'rb', 'Rashtrapati Bhavan', '1912–29', 1912, 'Edwin Lutyens, for the Raj', 20),
]
CENT = {  # colour = century of the principal fabric
    0: ('#3d3566', 'BCE – 5th c. CE'),
    11: ('#2c5878', '11th c.'), 12: ('#2f7480', '12th–13th c.'), 14: ('#3d8a6e', '14th c.'),
    15: ('#7d9a3c', '15th c.'), 16: ('#c49a1e', '16th c.'), 17: ('#d07a2a', '17th c.'),
    18: ('#b8432e', '18th c.'), 20: ('#7a2e4f', '20th c.'),
}
def ccol(yr):
    if yr < 1000: return CENT[0][0]
    c = yr // 100 + 1
    if c == 13: c = 12
    return CENT[c][0]

# icon placement: (dx, dy) offset of icon base from true point (0,0 = standing on it),
# label side & offset relative to icon base
PLACE = {
    'rb':      dict(off=(0, 0),    lab=('end', -36, 0)),
    'jantar':  dict(off=(0, 0),    lab=('end', -36, -12)),
    'kotla':   dict(off=(0, 0),    lab=('start', 26, -10)),
    'redfort': dict(off=(58, -22), lab=('start', 30, -6)),
    'sisganj': dict(off=(-24, -34), lab=('end', -22, -14)),
    'jama':    dict(off=(-46, 34), lab=('end', -28, -6)),
    'purana':  dict(off=(0, 0),    lab=('start', 26, -8)),
    'humayun': dict(off=(0, 0),    lab=('start', 38, -4)),
    'lodi':    dict(off=(0, 0),    lab=('middle', 0, -58)),
    'safdar':  dict(off=(-44, 30), lab=('end', -34, -8)),
    'siri':    dict(off=(0, 0),    lab=('start', 28, -6)),
    'jahan':   dict(off=(0, 0),    lab=('end', -32, -12)),
    'qutb':    dict(off=(0, 0),    lab=('start', 24, 0)),
    'lalkot':  dict(off=(-66, -6), lab=('middle', 0, -48)),
    'tughlaq': dict(off=(0, 0),    lab=('start', 30, -8)),
}

def esc(t): return t.replace('&', '&amp;')

out = []
o = out.append
o(f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" '
  'font-family="Georgia, \'Palatino Linotype\', \'Iowan Old Style\', serif">')
o('<title>How to Time Travel in Delhi</title>')
o(f'''<defs>
<clipPath id="mapclip"><rect x="{MX0}" y="{MY0}" width="{MX1-MX0}" height="{MY1-MY0}"/></clipPath>
<pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
<line x1="0" y1="0" x2="0" y2="6" stroke="{RULE}" stroke-width="0.6" opacity="0.35"/></pattern>
<filter id="plate" x="-0.04" y="-0.08" width="1.08" height="1.16"><feFlood flood-color="#efe6d2" flood-opacity="0.9"/><feComposite in="SourceGraphic" operator="over"/></filter>
<filter id="plate2" x="-0.03" y="-0.12" width="1.06" height="1.24"><feFlood flood-color="#efe6d2" flood-opacity="0.92"/><feComposite in="SourceGraphic" operator="over"/></filter>
</defs>''')
o(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
o(f'<rect x="6" y="6" width="{W-12}" height="{H-12}" fill="none" stroke="{RULE}" stroke-width="1.4"/>')
o(f'<rect x="11" y="11" width="{W-22}" height="{H-22}" fill="none" stroke="{RULE}" stroke-width="0.6"/>')

# ---------- title ----------
o(f'<text x="30" y="50" font-size="30" letter-spacing="3" fill="{INK}">HOW TO TIME TRAVEL IN DELHI</text>')
o(f'<text x="31" y="78" font-size="14" font-style="italic" fill="{SEPIA}">Fifteen standing monuments, a thousand years of capitals, all within about 13&#8201;km of Raisina Hill &#8212; '
  'with real walking and driving routes, and objects reaching back to the 1st millennium BCE.</text>')

# ---------- MAP ----------
o(f'<g clip-path="url(#mapclip)">')
o(f'<rect x="{MX0}" y="{MY0}" width="{MX1-MX0}" height="{MY1-MY0}" fill="#e9dfc6"/>')
bands = ['#e6dbbf', '#ece3cc', '#e6dbbf', '#ece3cc', '#e6dbbf']
for i in range(5, 0, -1):
    o(f'<circle cx="{CX:.1f}" cy="{CY:.1f}" r="{i*3*K}" fill="{bands[i-1]}"/>')
for i in range(1, 6):
    o(f'<circle cx="{CX:.1f}" cy="{CY:.1f}" r="{i*3*K}" fill="none" stroke="{RULE}" stroke-width="{2 if i==5 else 1}" opacity="0.8"/>')

# Yamuna
for e in Y['elements']:
    pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in (proj(g['lat'], g['lon']) for g in e['geometry']))
    o(f'<polyline points="{pts}" fill="none" stroke="#9fbcc0" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" opacity="0.75"/>')
    o(f'<polyline points="{pts}" fill="none" stroke="#7fa3a8" stroke-width="1" opacity="0.8"/>')
o(f'<text x="482" y="326" font-size="12" font-style="italic" letter-spacing="3" fill="#4f7479" transform="rotate(84 482 326)">YAMUNA</text>')

# district whispers
o(f'<g fill="{SEPIA}" opacity="0.5" font-style="italic" font-size="11" letter-spacing="1.5" text-anchor="middle">'
  f'<text x="130" y="131">SHAHJAHANABAD</text><text x="95" y="300">NEW DELHI</text>'
  f'<text x="540" y="560">NIZAMUDDIN</text><text x="150" y="975">MEHRAULI</text></g>')

# routes
def simplify(coords, tol=1.2):
    pts, last = [], None
    for lon, lat in coords:
        p = proj(lat, lon)
        if last is None or math.hypot(p[0]-last[0], p[1]-last[1]) >= tol:
            pts.append(p); last = p
    p = proj(coords[-1][1], coords[-1][0]); pts.append(p)
    return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
for k in ('drive1', 'drive2'):
    pts = simplify(R[k]['geom'])
    o(f'<polyline points="{pts}" fill="none" stroke="{BG}" stroke-width="5.5" stroke-linejoin="round" opacity="0.9"/>')
    o(f'<polyline points="{pts}" fill="none" stroke="{ROUTE}" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round" opacity="0.85"/>')
for k in ('walk1', 'walk2'):
    pts = simplify(R[k]['geom'], 0.8)
    o(f'<polyline points="{pts}" fill="none" stroke="{BG}" stroke-width="5" stroke-linejoin="round"/>')
    o(f'<polyline points="{pts}" fill="none" stroke="{ROUTE}" stroke-width="2.6" stroke-dasharray="0.1 4.4" stroke-linecap="round"/>')
o('</g>')
o(f'<rect x="{MX0}" y="{MY0}" width="{MX1-MX0}" height="{MY1-MY0}" fill="none" stroke="{RULE}" stroke-width="1.2"/>')

# ring labels where rings meet the west frame (3 km fully inside: its west point)
def ringlab(x, y, t):
    o(f'<g font-size="10.5" fill="{INK}"><rect x="{x}" y="{y-11}" width="{len(t)*5.6+8:.0f}" height="15" rx="2" fill="{BG}" opacity="0.92"/>'
      f'<text x="{x+4}" y="{y}">{t}</text></g>')
ringlab(CX - 3*K*0.866 - 17, CY - 3*K*0.5 + 4, '3 km')
for i in (2, 3, 4):
    r = i*3*K; yy = CY + math.sqrt(r*r - (CX-MX0)**2)
    ringlab(MX0 + 4, yy + 4, f'{i*3} km')
ringlab(600, 990, '15 km')

# site markers: true-position dot (+ leader) and miniature
order = sorted(SITES, key=lambda s: S[s[1]]['lat'], reverse=True)  # draw north first so southern icons overlap correctly
for n, sid, name, built, yr, who, cent in order:
    px, py = proj(S[sid]['lat'], S[sid]['lon'])
    dx, dy = PLACE[sid]['off']
    ix, iy = px + dx, py + dy
    col = CENT[cent][0]
    if (dx, dy) != (0, 0):
        o(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="{INK}" stroke-width="0.8" stroke-dasharray="2 2"/>')
    o(f'<ellipse cx="{ix:.1f}" cy="{iy+0.5:.1f}" rx="20" ry="3.2" fill="{INK}" opacity="0.18"/>')
    o(f'<g transform="translate({ix:.1f},{iy:.1f})" fill="{col}" stroke="{INK}" stroke-width="0.8" stroke-linejoin="round">{ICONS[sid]}</g>')
    o(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="2.6" fill="{INK}" stroke="{BG}" stroke-width="1"/>')
    anchor, lx, ly = PLACE[sid]['lab']
    tx, ty = ix + lx, iy + ly
    halo = f'paint-order="stroke" stroke="{BG}" stroke-width="3.5" stroke-linejoin="round"'
    # number badge sits before (start/middle) or after (end) the name
    nm = f'{n} · {name}' if anchor != 'end' else f'{name} · {n}'
    o('<g filter="url(#plate)">')
    o(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="{anchor}" font-size="12.5" font-weight="bold" fill="{INK}" {halo}>{esc(nm)}</text>')
    o(f'<text x="{tx:.1f}" y="{ty+13:.1f}" text-anchor="{anchor}" font-size="11" font-style="italic" fill="{col}" {halo}>{esc(built)}</text>')
    o('</g>')

# map legend box (NW corner, empty ground)
lx, ly = 452, 700
o(f'<rect x="{lx}" y="{ly}" width="184" height="124" rx="4" fill="{BG}" stroke="{RULE}" stroke-width="0.8" opacity="0.96"/>')
o(f'<line x1="{lx+10}" y1="{ly+18}" x2="{lx+38}" y2="{ly+18}" stroke="{ROUTE}" stroke-width="2.4"/>')
o(f'<text x="{lx+46}" y="{ly+22}" font-size="10.5" fill="{INK}">suggested drive (OSM roads)</text>')
o(f'<line x1="{lx+10}" y1="{ly+38}" x2="{lx+38}" y2="{ly+38}" stroke="{ROUTE}" stroke-width="2.6" stroke-dasharray="0.1 4.4" stroke-linecap="round"/>')
o(f'<text x="{lx+46}" y="{ly+42}" font-size="10.5" fill="{INK}">walking stretch</text>')
o(f'<circle cx="{lx+24}" cy="{ly+58}" r="2.6" fill="{INK}"/><line x1="{lx+24}" y1="{ly+58}" x2="{lx+36}" y2="{ly+52}" stroke="{INK}" stroke-width="0.8" stroke-dasharray="2 2"/>')
o(f'<text x="{lx+46}" y="{ly+62}" font-size="10.5" fill="{INK}">true spot (icon nudged)</text>')
o(f'<line x1="{lx+10}" y1="{ly+78}" x2="{lx+38}" y2="{ly+78}" stroke="#9fbcc0" stroke-width="7" stroke-linecap="round"/>')
o(f'<text x="{lx+46}" y="{ly+82}" font-size="10.5" fill="{INK}">Yamuna (today’s course)</text>')
o(f'<text x="{lx+10}" y="{ly+100}" font-size="10" font-style="italic" fill="{SEPIA}">icon colour = century founded</text>')
o(f'<text x="{lx+10}" y="{ly+114}" font-size="10" font-style="italic" fill="{SEPIA}">each 3 km ring ≈ 40 min walk</text>')

# north arrow + scale bar
o(f'<g transform="translate(622,150)"><polygon points="0,-24 6,8 0,1 -6,8" fill="{INK}"/>'
  f'<text y="-29" font-size="13" font-weight="bold" fill="{INK}" text-anchor="middle">N</text></g>')
o(f'<g transform="translate(470,985)"><rect width="{K}" height="7" fill="{INK}"/><rect x="{K}" width="{K}" height="7" fill="{BG}" stroke="{INK}" stroke-width="0.8"/>'
  f'<g font-size="10" fill="{INK}" text-anchor="middle"><text y="19">0</text><text x="{K}" y="19">1</text><text x="{2*K}" y="19">2 km</text></g></g>')

# Rashtrapati Bhavan tour callout
o(f'<g font-size="9.5" font-style="italic" fill="{SEPIA}" text-anchor="end">'
  f'<g filter="url(#plate)"><text x="{CX-36:.0f}" y="{CY+33:.0f}">map datum · Sanchi-style dome,</text>'
  f'<text x="{CX-36:.0f}" y="{CY+44:.0f}">Jaipur Column in the forecourt</text></g></g>')

# ---------- CHART: distance vs. depth (time runs left to right, oldest first) ----------
XL, XB0, XM, XR = 735, 835, 847, 1500
YT, YB = 175, 520
def tx(yr):
    if yr >= 1000: return XM + (yr - 1000) / 950 * (XR - XM)
    return XL + (yr + 1000) / 1500 * (XB0 - XL)
def ty(km): return YB - km / 14 * (YB - YT)

o(f'<text x="680" y="122" font-size="15" letter-spacing="2.5" fill="{INK}">HOW FAR YOU GO · HOW FAR BACK YOU GET</text>')
o(f'<text x="680" y="139" font-size="11" font-style="italic" fill="{SEPIA}">By year founded (earliest on the left), distance from Raisina (left axis) and walking time (right axis). Dashed lines: older objects re-used or dug up at the site.</text>')
# century bands tinted with the century colour => doubles as the colour key
for c in range(11, 21):
    x0, x1 = tx((c-1)*100), min(tx(c*100), XR)
    key = c if c in CENT else (12 if c == 13 else None)
    fill = CENT[key][0] if key else BG
    o(f'<rect x="{x0:.1f}" y="{YT}" width="{x1-x0:.1f}" height="{YB-YT}" fill="{fill}" opacity="{0.13 if key else 0.0}"/>')
    if c > 11:
        o(f'<line x1="{x0:.1f}" y1="{YT}" x2="{x0:.1f}" y2="{YB}" stroke="{RULE}" stroke-width="0.5" opacity="0.45"/>')
        o(f'<text x="{x0:.1f}" y="{YB+33}" font-size="8.5" text-anchor="middle" fill="{SEPIA}">{(c-1)*100}</text>')
    o(f'<text x="{(x0+x1)/2:.1f}" y="{YB+20}" font-size="10.5" text-anchor="middle" fill="{CENT[key][0] if key else SEPIA}" font-weight="{"bold" if key else "normal"}">{c}th c.</text>')
# compressed band for ancient objects, far left
o(f'<rect x="{XL}" y="{YT}" width="{XB0-XL}" height="{YB-YT}" fill="{ANCIENT}" opacity="0.10"/>')
for yr in (-500, 1, 500):
    o(f'<line x1="{tx(yr):.1f}" y1="{YT}" x2="{tx(yr):.1f}" y2="{YB}" stroke="{RULE}" stroke-width="0.5" opacity="0.45"/>')
o(f'<text x="{XL}" y="{YB+20}" font-size="9" fill="{ANCIENT}">1000 BCE</text>')
o(f'<text x="{tx(1):.1f}" y="{YB+33}" font-size="9" text-anchor="middle" fill="{ANCIENT}">1 CE</text>')
o(f'<text x="{(XL+XB0)/2:.1f}" y="{YT-6}" font-size="9" font-style="italic" text-anchor="middle" fill="{ANCIENT}">compressed scale</text>')
# axis break
o(f'<rect x="{XB0}" y="{YT+1}" width="{XM-XB0}" height="{YB-YT-2}" fill="{BG}"/>')
o(f'<path d="M{XB0-2},{YB+7} l4,-14 M{XM-2},{YB+7} l4,-14" stroke="{INK}" stroke-width="1"/>')
o(f'<rect x="{XL}" y="{YT}" width="{XR-XL}" height="{YB-YT}" fill="none" stroke="{RULE}" stroke-width="0.9"/>')
# distance axis (left) and walking time (right)
for km in range(0, 15, 2):
    o(f'<line x1="{XL-4}" y1="{ty(km):.1f}" x2="{XL}" y2="{ty(km):.1f}" stroke="{INK}" stroke-width="0.8"/>')
    o(f'<text x="{XL-8}" y="{ty(km)+3.5:.1f}" font-size="10" text-anchor="end" fill="{INK}">{km}</text>')
for km in (3, 6, 9, 12):
    o(f'<line x1="{XL}" y1="{ty(km):.1f}" x2="{XR}" y2="{ty(km):.1f}" stroke="{RULE}" stroke-width="0.6" opacity="0.35" stroke-dasharray="3 3"/>')
for h in (0, 1, 2, 3):
    y = ty(h * 4.5)
    o(f'<line x1="{XR}" y1="{y:.1f}" x2="{XR+4}" y2="{y:.1f}" stroke="{INK}" stroke-width="0.8"/>')
    o(f'<text x="{XR+7}" y="{y+3.5:.1f}" font-size="9.5" fill="{INK}">{h} h walk</text>')
o(f'<text transform="translate(702 {(YT+YB)/2}) rotate(-90)" font-size="10.5" text-anchor="middle" font-style="italic" fill="{SEPIA}">km from Raisina Hill, straight line (rings every 3 km)</text>')
o(f'<text x="{(XM+XR)/2:.1f}" y="{YB+50}" font-size="10.5" text-anchor="middle" font-style="italic" fill="{SEPIA}">year founded: earliest on the left, latest on the right</text>')

# trend: least squares year ~ km, drawn as km against year
pts = [(hav(S['rb'], S[sid]), yr) for n, sid, _, _, yr, _, _ in SITES]
mx = sum(p[0] for p in pts) / len(pts); my = sum(p[1] for p in pts) / len(pts)
slope = sum((x-mx)*(y-my) for x, y in pts) / sum((x-mx)**2 for x, _ in pts)
icpt = my - slope * mx
rr = sum((x-mx)*(y-my) for x, y in pts) / math.sqrt(sum((x-mx)**2 for x, _ in pts) * sum((y-my)**2 for _, y in pts))
print(f'fit: year = {icpt:.0f} {slope:+.1f}*km, r={rr:.2f}', file=sys.stderr)
o(f'<line x1="{tx(icpt+slope*13.5):.1f}" y1="{ty(13.5):.1f}" x2="{tx(icpt):.1f}" y2="{ty(0):.1f}" stroke="{INK}" stroke-width="1" stroke-dasharray="6 4" opacity="0.55"/>')
o(f'<g filter="url(#plate2)"><text x="{tx(1470):.1f}" y="{ty(12.9):.1f}" font-size="10.5" font-style="italic" fill="{INK}">- - -  rule of thumb: every km out ≈ {abs(slope):.0f} years back</text>'
  f'<text x="{tx(1470):.1f}" y="{ty(12.9)+13:.1f}" font-size="9.5" font-style="italic" fill="{SEPIA}">least-squares fit, r = {rr:.2f}. South is older; the Mughal north breaks it.</text></g>')

# older objects: dashed lines run left to when they were made
DROPS = [
    ('qutb', 400, 'Iron Pillar · c.400 CE'),
    ('kotla', -250, 'Ashokan Pillar · 3rd c. BCE · moved from Topra 1356'),
]
for sid, yr, t in DROPS:
    y = ty(hav(S['rb'], S[sid])); top = [s for s in SITES if s[1] == sid][0][4]
    o(f'<line x1="{tx(top):.1f}" y1="{y:.1f}" x2="{tx(yr):.1f}" y2="{y:.1f}" stroke="{ANCIENT}" stroke-width="1.1" stroke-dasharray="3 2.5"/>')
    o(f'<path d="M{tx(yr)-6:.1f},{y:.1f} l6,-6 l6,6 l-6,6 Z" fill="{ANCIENT}" stroke="{BG}" stroke-width="1"/>')
    o(f'<text x="{tx(yr)+9:.1f}" y="{y-7:.1f}" font-size="10" fill="{ANCIENT}" filter="url(#plate2)">{t}</text>')
y = ty(hav(S['rb'], S['purana']))
o(f'<line x1="{tx(1533):.1f}" y1="{y:.1f}" x2="{tx(0):.1f}" y2="{y:.1f}" stroke="{ANCIENT}" stroke-width="1.1" stroke-dasharray="3 2.5"/>')
o(f'<rect x="{tx(-1000):.1f}" y="{y-3.5:.1f}" width="{tx(0)-tx(-1000):.1f}" height="7" rx="3" fill="{ANCIENT}" opacity="0.45"/>')
o(f'<text x="{tx(-1000)+14:.1f}" y="{y+16:.1f}" font-size="10" fill="{ANCIENT}" filter="url(#plate2)">Painted Grey Ware sherds · 1st millennium BCE · dug up at Purana Qila</text>')

# points
for n, sid, name, built, yr, who, cent in SITES:
    x, y = tx(yr), ty(hav(S['rb'], S[sid]))
    o(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8.5" fill="{CENT[cent][0]}" stroke="{INK}" stroke-width="0.9"/>')
    o(f'<text x="{x:.1f}" y="{y+3.6:.1f}" font-size="{9.5 if n < 10 else 8.5}" font-weight="bold" text-anchor="middle" fill="{PAPER}">{n}</text>')

# ---------- KEY TABLE ----------
TY = 610
o(f'<text x="680" y="{TY-2}" font-size="15" letter-spacing="2.5" fill="{INK}">KEY · numbered by founding date</text>')
cols = [(680, '#'), (704, 'Monument'), (858, 'Built'), (968, 'Who built it'), (1268, 'Straight'), (1338, 'By road'), (1410, 'Walk'), (1476, 'Drive*')]
hy = TY + 20
for x, t in cols:
    anc = 'end' if t in ('Straight', 'By road', 'Walk', 'Drive*') else 'start'
    xx = x + 58 if anc == 'end' else x
    o(f'<text x="{xx}" y="{hy}" font-size="10" font-style="italic" fill="{SEPIA}" text-anchor="{anc}">{t}</text>')
o(f'<line x1="680" y1="{hy+6}" x2="1545" y2="{hy+6}" stroke="{RULE}" stroke-width="0.7"/>')
FD = R['fromDatum']
for i, (n, sid, name, built, yr, who, cent) in enumerate(SITES):
    y = hy + 24 + i * 24.5
    if i % 2 == 0:
        o(f'<rect x="676" y="{y-15}" width="873" height="24.5" fill="{RULE}" opacity="0.06"/>')
    col = CENT[cent][0]
    o(f'<circle cx="688" cy="{y-4}" r="8" fill="{col}" stroke="{INK}" stroke-width="0.7"/>')
    o(f'<text x="688" y="{y-0.5}" font-size="{9 if n<10 else 8}" font-weight="bold" text-anchor="middle" fill="{PAPER}">{n}</text>')
    o(f'<text x="704" y="{y}" font-size="12" font-weight="bold" fill="{INK}">{esc(name)}</text>')
    o(f'<text x="858" y="{y}" font-size="11.5" fill="{col}" font-weight="bold">{esc(built)}</text>')
    o(f'<text x="968" y="{y}" font-size="11" font-style="italic" fill="{SEPIA}">{esc(who)}</text>')
    d = hav(S['rb'], S[sid])
    if sid == 'rb':
        vals = ('datum', '—', '—', '—')
    else:
        f = FD[sid]
        wm = f['foot']['min']
        vals = (f'{d:.1f} km', f'{f["car"]["km"]:.1f} km', f'{wm//60} h {wm%60:02d}' if wm >= 60 else f'{wm} min', f'{f["car"]["min"]} min')
    for (x, _), v in zip(cols[4:], vals):
        o(f'<text x="{x+58}" y="{y}" font-size="11.5" text-anchor="end" fill="{INK}">{v}</text>')
ty_end = hy + 24 + 15 * 24.5
o(f'<text x="680" y="{ty_end-4:.0f}" font-size="9.5" font-style="italic" fill="{SEPIA}">Road distance, walk and drive times from Raisina via OpenStreetMap routing (FOSSGIS OSRM). '
  '*Drive times are free-flow: Delhi traffic typically makes them 2–3× longer.</text>')

# ---------- FOOTER ----------
FY = 1040
o(f'<line x1="30" y1="{FY-14}" x2="1570" y2="{FY-14}" stroke="{RULE}" stroke-width="0.7"/>')
d_km = R['drive1']['km'] + R['drive2']['km']; d_min = R['drive1']['min'] + R['drive2']['min']
w_km = R['walk1']['km'] + R['walk2']['km']; w_min = R['walk1']['min'] + R['walk2']['min']
o(f'<text x="30" y="{FY+6}" font-size="13" letter-spacing="2" fill="{INK}">THE SUGGESTED DAY · DRIVE SOUTH INTO THE PAST</text>')
foot1 = [
    f'15 Rashtrapati Bhavan → 12 Jantar Mantar → 14 Sis Ganj; walk Chandni Chowk to 10 Red Fort and 11 Jama Masjid ({R["walk1"]["km"]:.1f} km, ~{R["walk1"]["min"]} min); drive 6 Kotla → 8 Purana Qila → 9 Humayun → 7 Lodi → 13 Safdarjung → 3 Siri',
    f'→ 4 Tughlaqabad → 5 Jahanpanah → 2 Qutb; walk to 1 Lal Kot ({R["walk2"]["km"]:.1f} km). Driving {d_km:.0f} km (~{d_min} min free-flow, realistically 3+ hours); walking {w_km:.1f} km (~{w_min} min). Broadly, you start in 1912 and end in c.1060.',
]
for i, t in enumerate(foot1):
    o(f'<text x="30" y="{FY+26+i*15}" font-size="11" fill="{INK}">{esc(t)}</text>')
o(f'<text x="30" y="{FY+66}" font-size="9.5" font-style="italic" fill="{SEPIA}">Positions: Wikipedia/OpenStreetMap coordinates, local equirectangular projection centred on Raisina (28.6143° N, 77.1994° E), north up, 44 px/km. '
  'Jahanpanah is plotted at Bijay Mandal; Siri and Lal Kot at surviving wall sections.</text>')
o(f'<text x="30" y="{FY+79}" font-size="9.5" font-style="italic" fill="{SEPIA}">Rings are straight-line distance at 4.5 km/h walking, after Galton’s isochronic passage chart (1881) and Bartholomew’s isochronic map (1914). '
  'Dates: ASI, UNESCO, Delhi SRDC and cited Wikipedia sources. Road and river data © OpenStreetMap contributors (ODbL).</text>')
o('</svg>')

open(sys.argv[1], 'w').write('\n'.join(out))
