# Close-up map of Lutyens' Delhi: the whole major-road network in grey, the 1920s ruler- and
# viceroy-named roads coloured by era with their names along them, and nearby monuments.
# make_streetmap() returns (svg_markup, label_report). Labels are placed greedily and checked
# for collisions with each other, the monument figures and the frame.
import json, math, sys
from PIL import ImageFont
from icons import ICONS, INK, PAPER
import streets_data as SD

_argv = sys.argv; sys.argv = ['build.py', '/dev/null']
import build as B                      # site catalogue, colours, coordinates
sys.argv = _argv

LAT0, LAT1, LON0, LON1 = 28.578, 28.640, 77.186, 77.253
K = 125                                 # px per km
X0, Y0 = 10, 10
LATC = (LAT0 + LAT1) / 2
W = (LON1 - LON0) * math.cos(math.radians(LATC)) * 111.32 * K
H = (LAT1 - LAT0) * 110.574 * K
SEPIA, RULE = '#5b4a36', '#6b5942'
GEORGIA = '/System/Library/Fonts/Supplemental/Georgia.ttf'
GEORGIA_I = '/System/Library/Fonts/Supplemental/Georgia Italic.ttf'
GEORGIA_B = '/System/Library/Fonts/Supplemental/Georgia Bold.ttf'

def P(lat, lon):
    return (X0 + (lon - LON0) * math.cos(math.radians(LATC)) * 111.32 * K,
            Y0 + (LAT1 - lat) * 110.574 * K)

# ---------- geometry helpers for collision tests (rotated rectangles, separating axes) ----------
def rect(cx, cy, w, h, ang):
    a = math.radians(ang); c, s = math.cos(a), math.sin(a)
    return [(cx + dx * c - dy * s, cy + dx * s + dy * c) for dx, dy in ((-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2))]

def overlap(A, Bp):
    for poly in (A, Bp):
        for i in range(len(poly)):
            x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % len(poly)]
            nx, ny = y2 - y1, x1 - x2
            pa = [nx * x + ny * y for x, y in A]; pb = [nx * x + ny * y for x, y in Bp]
            if max(pa) < min(pb) or max(pb) < min(pa):
                return False
    return True

def inside_frame(poly, pad=4):
    return all(X0 + pad < x < X0 + W - pad and Y0 + pad < y < Y0 + H - pad for x, y in poly)

# ---------- India Gate (not in the main catalogue, so it gets its own small figure) ----------
INDIA_GATE = (28.612912, 77.229510)
INDIA_GATE_ICON = ('<rect x="-12" y="-30" width="24" height="30"/>'
                   '<path d="M-5,0 V-14 A5,5 0 0 1 5,-14 V0 Z" fill="#f6efdf" stroke="none"/>'
                   '<rect x="-14" y="-34" width="28" height="4"/><path d="M-6,-34 Q0,-41 6,-34 Z"/>')

def make_streetmap():
    roads = json.load(open('closeup_roads.json'))['elements'] + json.load(open('kalam_lane.json'))['elements']
    named = {n: i for i, s in enumerate(SD.STREETS) for n in s[0]}
    o = []
    o.append(f'<svg viewBox="0 0 {W + 2*X0:.0f} {H + 2*Y0:.0f}" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, \'Palatino Linotype\', serif" role="img" aria-label="Close-up map of Lutyens\' Delhi with 1920s street names coloured by era">')
    o.append(f'<defs><clipPath id="sclip"><rect x="{X0}" y="{Y0}" width="{W:.1f}" height="{H:.1f}"/></clipPath>'
             f'<filter id="splate" x="-0.04" y="-0.12" width="1.08" height="1.24"><feFlood flood-color="{PAPER}" flood-opacity="0.92"/><feComposite in="SourceGraphic" operator="over"/></filter></defs>')
    o.append(f'<rect x="{X0}" y="{Y0}" width="{W:.1f}" height="{H:.1f}" fill="#ece3cc"/>')
    o.append('<g clip-path="url(#sclip)">')
    # river
    for e in B.Y['elements']:
        pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in (P(g['lat'], g['lon']) for g in e['geometry']))
        o.append(f'<polyline points="{pts}" fill="none" stroke="#9fbcc0" stroke-width="12" stroke-linecap="round" opacity=".7"/>')
    # grey network
    o.append('<g fill="none" stroke="#b9ab8e" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">')
    for e in roads:
        if e['tags'].get('name') in named: continue
        o.append('<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in (P(g['lat'], g['lon']) for g in e['geometry'])) + '"/>')
    o.append('</g>')
    # era streets
    lines = {}
    for e in roads:
        i = named.get(e['tags'].get('name'))
        if i is None: continue
        lines.setdefault(i, []).append([P(g['lat'], g['lon']) for g in e['geometry']])
    def chain(ls):
        # join pieces that share an endpoint (OSM splits one road into many ways)
        ls = [list(l) for l in ls]; joined = True
        close = lambda a, b: math.dist(a, b) < 0.8
        while joined:
            joined = False
            for a in range(len(ls)):
                for b in range(len(ls)):
                    if a == b: continue
                    A, Bl = ls[a], ls[b]
                    if close(A[-1], Bl[0]): ls[a] = A + Bl[1:]
                    elif close(A[-1], Bl[-1]): ls[a] = A + Bl[::-1][1:]
                    elif close(A[0], Bl[-1]): ls[a] = Bl + A[1:]
                    elif close(A[0], Bl[0]): ls[a] = Bl[::-1] + A[1:]
                    else: continue
                    del ls[b]; joined = True; break
                if joined: break
        return ls
    lines = {i: chain(ls) for i, ls in lines.items()}
    colour = SD.colour
    pstr = lambda l: ' '.join(f'{x:.1f},{y:.1f}' for x, y in l)
    # the suggested route from the main map: a soft band under the coloured roads, a thin line over them
    ROUTE = '#8a2f1f'
    route = {k: [P(lat, lon) for lon, lat in B.R[k]['geom']] for k in ('drive1', 'drive2', 'walk1', 'walk2')}
    o.append(f'<g class="sroute" pointer-events="none" fill="none" stroke="{ROUTE}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" opacity=".3">')
    for k, l in route.items(): o.append(f'<polyline points="{pstr(l)}"/>')
    o.append('</g>')
    o.append(f'<g fill="none" stroke="{PAPER}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round">')
    for ls in lines.values():
        for l in ls: o.append(f'<polyline points="{pstr(l)}"/>')
    o.append('</g>')
    for i, ls in lines.items():
        col = colour(SD.STREETS[i][4])
        o.append(f'<g class="lstreet" data-i="{i}">')
        for l in ls:
            o.append(f'<polyline class="case" points="{pstr(l)}" fill="none" stroke="{PAPER}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
                     f'<polyline class="vis" points="{pstr(l)}" fill="none" stroke="{col}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
                     f'<polyline points="{pstr(l)}" fill="none" stroke="transparent" stroke-width="14"/>')
        o.append('</g>')
    o.append(f'<g class="sroute" pointer-events="none" fill="none" stroke="{ROUTE}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" opacity=".9">')
    for k, l in route.items():
        dash = ' stroke-dasharray="0.1 4" stroke-width="2.4"' if k.startswith('walk') else ''
        o.append(f'<polyline points="{pstr(l)}"{dash}/>')
    o.append('</g>')
    # densified points of every coloured street, so labels can avoid sitting on them
    road_pts = []
    for i, ls in lines.items():
        for l in ls:
            for k in range(len(l) - 1):
                n = max(1, int(math.dist(l[k], l[k+1]) / 3))
                road_pts += [(i, l[k][0] + (l[k+1][0] - l[k][0]) * t / n, l[k][1] + (l[k+1][1] - l[k][1]) * t / n) for t in range(n)]
    def covers(poly, own=None):
        xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
        bx0, bx1, by0, by1 = min(xs), max(xs), min(ys), max(ys)
        for j, x, y in road_pts:
            if j == own or not (bx0 <= x <= bx1 and by0 <= y <= by1): continue
            if overlap(poly, [(x-1, y-1), (x+1, y-1), (x+1, y+1), (x-1, y+1)]): return True
        return False
    o.append('</g>')

    # ---------- monuments ----------
    obstacles = []
    mons = []
    for n, sid, name, built, yr, who, cent in B.SITES:
        x, y = P(B.S[sid]['lat'], B.S[sid]['lon'])
        if X0 + 20 < x < X0 + W - 20 and Y0 + 50 < y < Y0 + H - 5:
            mons.append((sid, f'{n} · {name}', x, y, B.CENT[cent][0], ICONS[sid]))
    gx, gy = P(*INDIA_GATE)
    mons.append(('indiagate', 'India Gate · 1931', gx, gy, B.CENT[20][0], INDIA_GATE_ICON))
    f_mon = ImageFont.truetype(GEORGIA_B, 11)
    for sid, label, x, y, col, icon in mons:
        o.append(f'<g class="lmon" data-id="{sid}"><ellipse cx="{x:.1f}" cy="{y+0.5:.1f}" rx="18" ry="3" fill="{INK}" opacity=".18"/>'
                 f'<g transform="translate({x:.1f},{y:.1f}) scale(0.85)" fill="{col}" stroke="{INK}" stroke-width="0.9" stroke-linejoin="round">{icon}</g>'
                 f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="{INK}"/></g>')
        obstacles.append(rect(x, y - 24, 52, 52, 0))
    # whisper and legend go in first, so street labels keep clear of them
    cpx, cpy = P(28.6315, 77.2167)
    f_w = ImageFont.truetype(GEORGIA_I, 10.5)
    obstacles.append(rect(cpx, cpy - 4, f_w.getlength('CONNAUGHT PLACE') * 1.15 + 6, 15, 0))
    LEG = [(0, 'Ancient'), (12, 'Rajput'), (14, 'Delhi Sultanate (14th c.)'), (15, 'Delhi Sultanate (15th c.)'), (16, 'Sur and Mughal (16th c.)'),
           (17, 'Mughal (17th c.)'), (18, 'Late Mughal (18th c.)'), ('eu', 'British and European'), (None, 'Jai Singh of Amber (I or II?)'), ('other', 'Other renaming since 2014')]
    lw, lh = 236, 34 + 15 * len(LEG) + 45
    lx, ly = X0 + 8, Y0 + H - lh - 8
    obstacles.append([(lx, ly), (lx + lw, ly), (lx + lw, ly + lh), (lx, ly + lh)])
    leg = [f'<g class="slegend"><rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" rx="3" fill="{PAPER}" stroke="{RULE}" stroke-width=".8" opacity=".97"/>',
           f'<text x="{lx+10}" y="{ly+18}" font-size="11" font-weight="bold" fill="{INK}">Named after… (colour = namesake’s era)</text>']
    for k, (era, name) in enumerate(LEG):
        yy = ly + 34 + 15 * k
        leg.append(f'<line x1="{lx+10}" y1="{yy-3.5}" x2="{lx+34}" y2="{yy-3.5}" stroke="{colour(era)}" stroke-width="4" stroke-linecap="round"/>'
                   f'<text x="{lx+42}" y="{yy}" font-size="10" fill="{INK}">{name}</text>')
    yy = ly + 34 + 15 * len(LEG) + 4
    leg.append(f'<line x1="{lx+10}" y1="{yy-3.5}" x2="{lx+34}" y2="{yy-3.5}" stroke="#b9ab8e" stroke-width="1.6"/><text x="{lx+42}" y="{yy}" font-size="10" fill="{SEPIA}">other major roads</text>')
    yy += 15
    leg.append(f'<line x1="{lx+10}" y1="{yy-3.5}" x2="{lx+34}" y2="{yy-3.5}" stroke="{ROUTE}" stroke-width="10" opacity=".3" stroke-linecap="round"/>'
               f'<line x1="{lx+10}" y1="{yy-3.5}" x2="{lx+34}" y2="{yy-3.5}" stroke="{ROUTE}" stroke-width="1.6"/><text x="{lx+42}" y="{yy}" font-size="10" fill="{INK}">the suggested route (main map)</text>')
    leg.append(f'<text x="{lx+10}" y="{yy+17}" font-size="9.5" font-style="italic" fill="{SEPIA}">Labels: today’s name, older names in brackets</text></g>')

    # monument labels: try right, left, below
    mon_labels = []
    for sid, label, x, y, col, icon in mons:
        w = f_mon.getlength(label) + 8; h = 16
        cands = [(x + 28 + w/2, y - 12, 'start'), (x - 28 - w/2, y - 12, 'end'), (x, y + 14, 'middle'), (x, y - 62, 'middle'),
                 (x + 28 + w/2, y - 30, 'start'), (x - 28 - w/2, y - 30, 'end'), (x + 28 + w/2, y + 6, 'start'), (x - 28 - w/2, y + 6, 'end')]
        ok = lambda R: inside_frame(R) and not any(overlap(R, ob) for ob in obstacles)
        cands = [c for c in cands if ok(rect(c[0], c[1], w, h, 0))]
        cands.sort(key=lambda c: covers(rect(c[0], c[1], w, h, 0)))
        for cx, cy, anchor in cands[:1]:
            R = rect(cx, cy, w, h, 0)
            if True:
                tx = {'start': cx - w/2 + 4, 'end': cx + w/2 - 4, 'middle': cx}[anchor]
                mon_labels.append(f'<text x="{tx:.1f}" y="{cy+4:.1f}" text-anchor="{anchor}" font-size="11" font-weight="bold" fill="{INK}" filter="url(#splate)">{label}</text>')
                obstacles.append(R); break

    # ---------- street labels along the roads ----------
    # ---------- street labels: today's name, older name(s) in brackets on a second line ----------
    f1, f2 = ImageFont.truetype(GEORGIA, 10), ImageFont.truetype(GEORGIA_I, 8.8)
    FIRST = ['Kingsway', 'Queensway', 'Aurangzeb Road', 'Dalhousie Road', 'Race Course Road', 'Curzon Road']
    order = sorted(lines, key=lambda i: (SD.STREETS[i][1] not in FIRST, FIRST.index(SD.STREETS[i][1]) if SD.STREETS[i][1] in FIRST else 0,
                                         SD.STREETS[i][4] in ('eu', 'other'), -sum(len(l) for l in lines[i])))
    placed, report = [], {}
    def fits(R, i, strict):
        return inside_frame(R) and not any(overlap(R, ob) for ob in obstacles + placed) and not (strict and covers(R, own=i))
    for i in order:
        old = SD.STREETS[i][1]
        line1, line2 = SD.names(old)
        tw = max(f1.getlength(line1), f2.getlength(line2) if line2 else 0) * 1.06 + 6
        th = 13 if not line2 else 24
        best = None
        for strict in (True, False):
            for l in sorted(lines[i], key=lambda l: -sum(math.dist(l[k], l[k+1]) for k in range(len(l)-1))):
                cum = [0]
                for k in range(len(l) - 1): cum.append(cum[-1] + math.dist(l[k], l[k+1]))
                def at(d):
                    for k in range(len(l) - 1):
                        if cum[k+1] >= d:
                            t = (d - cum[k]) / max(cum[k+1] - cum[k], 1e-9)
                            return (l[k][0] + t * (l[k+1][0] - l[k][0]), l[k][1] + t * (l[k+1][1] - l[k][1]))
                    return l[-1]
                total = cum[-1]
                if total < tw * 0.9: continue
                for s0 in [total/2 - tw/2] + list(range(0, int(total - tw) + 1, 8)):
                    a, b = at(max(s0, 0)), at(min(s0 + tw, total))
                    if math.dist(a, b) < tw * 0.85: continue                    # too curved here
                    ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
                    ang = ang - 180 if ang > 90 else ang + 180 if ang < -90 else ang
                    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
                    nx, ny = -math.sin(math.radians(ang)), math.cos(math.radians(ang))
                    for side in (-1, 1):
                        cx, cy = mx + side * nx * (th/2 + 3), my + side * ny * (th/2 + 3)
                        R = rect(cx, cy, tw, th, ang)
                        if fits(R, i, strict): best = (cx, cy, ang, R); break
                    if best: break
                if best: break
            if best: break
        if not best:
            # fallback for roads split by roundabouts: follow the road's overall direction through its middle
            pts_ = [q for l in lines[i] for q in l]
            mx_ = sum(q[0] for q in pts_) / len(pts_); my_ = sum(q[1] for q in pts_) / len(pts_)
            sxx = sum((q[0]-mx_)**2 for q in pts_); syy = sum((q[1]-my_)**2 for q in pts_); sxy = sum((q[0]-mx_)*(q[1]-my_) for q in pts_)
            ang = math.degrees(0.5 * math.atan2(2 * sxy, sxx - syy))
            ang = ang - 180 if ang > 90 else ang + 180 if ang < -90 else ang
            ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang)); nx, ny = -uy, ux
            proj = [(q[0]-mx_)*ux + (q[1]-my_)*uy for q in pts_]
            for strict in (True, False):
                for along in (0, -0.2, 0.2, -0.35, 0.35):
                    c0 = (min(proj) + max(proj)) / 2 + along * (max(proj) - min(proj))
                    for off in (-(th/2 + 3), th/2 + 3, -(th/2 + 9), th/2 + 9):
                        cx, cy = mx_ + ux * c0 + nx * off, my_ + uy * c0 + ny * off
                        R = rect(cx, cy, tw, th, ang)
                        if fits(R, i, strict): best = (cx, cy, ang, R); break
                    if best: break
                if best: break
        leader = None
        if not best:
            # last resort: a horizontal label close by, with a thin pointer to the road
            pts_ = [q for l in lines[i] for q in l]
            mid = min(pts_, key=lambda q: math.dist(q, (sum(p[0] for p in pts_)/len(pts_), sum(p[1] for p in pts_)/len(pts_))))
            for strict in (True, False):
                for r in range(24, 200, 8):
                    for k in range(16):
                        t = math.radians(k * 22.5)
                        cx, cy = mid[0] + r * math.cos(t), mid[1] + r * math.sin(t)
                        R = rect(cx, cy, tw, th, 0)
                        if fits(R, i, strict): best, leader = (cx, cy, 0, R), mid; break
                    if best: break
                if best: break
        if best:
            cx, cy, ang, R = best; placed.append(R)
            if leader:
                ex = max(min(leader[0], cx + tw/2), cx - tw/2); ey = cy + (th/2 if leader[1] > cy else -th/2)
                o.append(f'<line class="sleader" data-i="{i}" x1="{leader[0]:.1f}" y1="{leader[1]:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{INK}" stroke-width=".7" stroke-dasharray="2 2"/>')
            halo = f'paint-order="stroke" stroke="{PAPER}" stroke-width="3" stroke-linejoin="round"'
            if line2:
                body = (f'<text y="-2" font-size="10" fill="{INK}" {halo}>{line1}</text>'
                        f'<text y="9.5" font-size="8.8" font-style="italic" fill="{SEPIA}" {halo}>{line2}</text>')
            else:
                body = f'<text y="3.5" font-size="10" fill="{INK}" {halo}>{line1}</text>'
            o.append(f'<g class="slabel" data-i="{i}" transform="translate({cx:.1f} {cy:.1f}) rotate({ang:.1f})" text-anchor="middle">{body}</g>')
            report[old] = 'placed'
        else:
            report[old] = 'no room'
    o.extend(mon_labels)
    o.extend(leg)
    # whispers, frame, north arrow, scale bar
    o.append(f'<text x="{cpx:.1f}" y="{cpy:.1f}" text-anchor="middle" font-size="10.5" font-style="italic" letter-spacing="1.5" fill="{SEPIA}" opacity=".75">CONNAUGHT PLACE</text>')
    o.append(f'<rect x="{X0}" y="{Y0}" width="{W:.1f}" height="{H:.1f}" fill="none" stroke="{RULE}" stroke-width="1.2"/>')
    o.append(f'<g transform="translate({X0 + W - 22:.1f},{Y0 + 40})"><polygon points="0,-22 5,7 0,1 -5,7" fill="{INK}"/><text y="-27" font-size="12" font-weight="bold" fill="{INK}" text-anchor="middle">N</text></g>')
    sx, sy = X0 + W - 140, Y0 + H - 18
    o.append(f'<g transform="translate({sx:.1f},{sy:.1f})"><rect x="-6" y="-14" width="128" height="30" fill="{PAPER}" opacity=".85"/><rect width="{K/2:.1f}" height="6" fill="{INK}"/><rect x="{K/2:.1f}" width="{K/2:.1f}" height="6" fill="{PAPER}" stroke="{INK}" stroke-width=".8"/>'
             f'<g font-size="9.5" fill="{INK}" text-anchor="middle"><text y="-4">0</text><text x="{K/2:.1f}" y="-4">0.5</text><text x="{K:.1f}" y="-4">1 km</text></g></g>')
    o.append('</svg>')
    return '\n'.join(o), report

if __name__ == '__main__':
    svg, rep = make_streetmap()
    open(sys.argv[1] if len(sys.argv) > 1 else 'streetmap_preview.svg', 'w').write(svg)
    print({k: v for k, v in rep.items() if v != 'placed'} or 'all labels placed', f'{W:.0f}x{H:.0f}')
