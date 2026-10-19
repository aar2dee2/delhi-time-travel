# Miniature monuments. Each is drawn with its base centre at (0,0), growing upward (negative y).
# Main masses take the <use> element's fill (= century colour); details use PAPER / ANCIENT.
PAPER = '#f6efdf'
ANCIENT = '#3d3566'
INK = '#2a2118'

def arches(xs, y, w, h):
    """Row of small pointed arch openings, base at y."""
    out = []
    for x in xs:
        out.append(f'<path d="M{x-w/2},{y} V{y-h*0.6} Q{x-w/2},{y-h} {x},{y-h} Q{x+w/2},{y-h} {x+w/2},{y-h*0.6} V{y} Z" fill="{PAPER}" stroke="none"/>')
    return ''.join(out)

def dome(cx, base, r, h=None, finial=4):
    """Bulbous dome (slightly onion) standing on `base`."""
    h = h or r * 1.25
    return (f'<path d="M{cx-r},{base} C{cx-r*1.15},{base-h*0.55} {cx-r*0.45},{base-h*0.9} {cx},{base-h} '
            f'C{cx+r*0.45},{base-h*0.9} {cx+r*1.15},{base-h*0.55} {cx+r},{base} Z"/>'
            f'<line x1="{cx}" y1="{base-h}" x2="{cx}" y2="{base-h-finial}" stroke-width="1"/>')

def chhatri(cx, base, w=6):
    return (f'<rect x="{cx-w/2}" y="{base-3}" width="{w}" height="3"/>'
            + dome(cx, base-3, w/2, w*0.55, 2))

def merlons(x0, x1, y, step=4, w=2.4, h=2.4):
    out, x = [], x0
    while x + w <= x1 + 0.01:
        out.append(f'<rect x="{x:.1f}" y="{y-h}" width="{w}" height="{h}"/>')
        x += step
    return ''.join(out)

ICONS = {}

# 1 Lal Kot: ruined rubble rampart with one great round bastion
ICONS['lalkot'] = (
    '<path d="M-24,0 L-24,-10 L-20,-12 L-17,-9 L-13,-13 L-9,-11 L-9,0 Z"/>'
    '<path d="M-9,0 V-20 A9,9 0 0 1 9,-20 V0 Z"/>'
    '<path d="M9,0 V-12 L13,-14 L16,-10 L20,-12 L24,-8 L24,0 Z"/>'
    + ''.join(f'<path d="M{a},{b} h4" stroke="{PAPER}" stroke-width="0.8"/>' for a, b in
              [(-21, -4), (-15, -7), (-5, -6), (1, -12), (-3, -16), (12, -4), (17, -7), (3, -3)])
)

# 2 Qutb Minar (fluted, 5 storeys, balconies) + Gupta Iron Pillar beside it
q = ['<path d="M-8,0 L-3.2,-58 L3.2,-58 L8,0 Z"/>']
for yb in (-16, -29, -40, -49, -55):
    hw = 8 - (8 - 3.2) * (-yb / 58) + 1.6
    q.append(f'<rect x="{-hw:.1f}" y="{yb-1.6}" width="{2*hw:.1f}" height="2.2"/>')
for xf in (-4.5, -1.5, 1.5, 4.5):
    q.append(f'<line x1="{xf}" y1="-1" x2="{xf*0.45:.1f}" y2="-15" stroke="{PAPER}" stroke-width="0.6"/>')
q.append('<path d="M-2.2,-58 Q0,-63 2.2,-58 Z"/>')
q.append(f'<g fill="{ANCIENT}"><rect x="13" y="-17" width="2.6" height="17"/><rect x="12" y="-20" width="4.6" height="3"/></g>')
ICONS['qutb'] = ''.join(q)

# 3 Siri: straight curtain wall with three round bastions and loopholes
s = ['<rect x="-24" y="-13" width="48" height="13"/>']
for bx in (-18, 0, 18):
    s.append(f'<path d="M{bx-5},0 V-17 A5,5 0 0 1 {bx+5},-17 V0 Z"/>')
    s.append(f'<rect x="{bx-0.7}" y="-13" width="1.4" height="4" fill="{PAPER}" stroke="none"/>')
s.append(merlons(-23, -6, -13) + merlons(5, 23, -13))
ICONS['siri'] = ''.join(s)

# 4 Tughlaqabad: massive battered (sloping) bastions
ICONS['tughlaq'] = (
    '<path d="M-26,0 L-22,-32 L-12,-32 L-8,0 Z"/>'
    '<path d="M8,0 L12,-32 L22,-32 L26,0 Z"/>'
    '<path d="M-9,0 L-8,-24 H8 L9,0 Z"/>'
    + merlons(-22, -12, -32, 3.6, 2.2, 2.6) + merlons(12, 22, -32, 3.6, 2.2, 2.6) + merlons(-7.5, 7.5, -24, 3.8, 2.2, 2.2)
    + arches([0], 0, 6, 11)
    + f'<line x1="-24" y1="-12" x2="-10" y2="-12" stroke="{PAPER}" stroke-width="0.6"/>'
      f'<line x1="10" y1="-12" x2="24" y2="-12" stroke="{PAPER}" stroke-width="0.6"/>'
)

# 5 Jahanpanah / Bijay Mandal: stepped high platform with domed pavilion
ICONS['jahan'] = (
    '<path d="M-24,0 L-20,-12 H20 L24,0 Z"/>'
    '<path d="M-15,-12 L-12,-21 H12 L15,-12 Z"/>'
    '<rect x="-6.5" y="-31" width="13" height="10"/>'
    + arches([0], -21, 5, 8) + dome(0, -31, 6.5, 7, 3)
    + arches([-14, -7, 0, 7, 14], 0, 3.5, 7)
)

# 6 Feroz Shah Kotla: three arcaded tiers carrying the Ashokan pillar
k = ['<rect x="-21" y="-9" width="42" height="9"/>', '<rect x="-15" y="-18" width="30" height="9"/>',
     '<rect x="-9" y="-27" width="18" height="9"/>']
k.append(arches([-16, -10, -4, 4, 10, 16], 0, 3.6, 7))
k.append(arches([-10, -4, 4, 10], -9, 3.6, 7))
k.append(arches([-4, 4], -18, 3.6, 7))
k.append(f'<g fill="{ANCIENT}"><path d="M-1.8,-27 L-1.3,-55 H1.3 L1.8,-27 Z"/><circle cx="0" cy="-56.5" r="2"/></g>')
ICONS['kotla'] = ''.join(k)

# 7 Lodi tombs: octagonal tomb, verandah of arches, single dome ringed by chhatris
ICONS['lodi'] = (
    '<path d="M-19,0 V-13 L-16,-16 H16 L19,-13 V0 Z"/>'
    + arches([-13, -6.5, 0, 6.5, 13], 0, 4.4, 9)
    + '<rect x="-10" y="-20" width="20" height="4"/>'
    + dome(0, -20, 10, 12, 4)
    + chhatri(-14, -16) + chhatri(14, -16)
)

# 8 Purana Qila: Bara Darwaza, gate between round towers, chhatris above
ICONS['purana'] = (
    '<rect x="-12" y="-28" width="24" height="28"/>'
    + arches([0], 0, 11, 20)
    + '<path d="M-22,0 V-27 A5,5 0 0 1 -12,-27 V0 Z"/><path d="M12,0 V-27 A5,5 0 0 1 22,-27 V0 Z"/>'
    + chhatri(-6, -28, 6) + chhatri(6, -28, 6)
    + f'<rect x="-9" y="-25" width="18" height="2" fill="{PAPER}" stroke="none"/>'
)

# 9 Humayun's Tomb: arcaded plinth, iwan, double dome, chhatris
ICONS['humayun'] = (
    '<rect x="-28" y="-8" width="56" height="8"/>'
    + arches([-23, -16, -9, -2, 5, 12, 19, 26][:-1], 0, 4, 6) + arches([23], 0, 4, 6)
    + '<rect x="-17" y="-25" width="34" height="17"/>'
    + arches([0], -8, 9, 15) + arches([-12, 12], -8, 4.5, 9)
    + '<rect x="-8" y="-29" width="16" height="4"/>'
    + dome(0, -29, 9.5, 15, 5)
    + chhatri(-12, -25, 6) + chhatri(12, -25, 6)
)

# 10 Red Fort: Lahori Gate — crenellated wall, gate, row of chhatris, octagonal turrets
ICONS['redfort'] = (
    '<rect x="-26" y="-16" width="52" height="16"/>'
    + merlons(-25, -11, -16, 3.6, 2.2, 2.4) + merlons(11, 25, -16, 3.6, 2.2, 2.4)
    + '<rect x="-11" y="-26" width="22" height="26"/>'
    + arches([0], 0, 9, 18)
    + ''.join(chhatri(x, -26, 3.6) for x in (-7.5, -3.75, 0, 3.75, 7.5))
    + '<rect x="-15" y="-34" width="4" height="34"/><rect x="11" y="-34" width="4" height="34"/>'
    + chhatri(-13, -34, 6) + chhatri(13, -34, 6)
)

# 11 Jama Masjid: three striped domes, two minarets
j = ['<rect x="-24" y="-7" width="48" height="7"/>', '<rect x="-15" y="-19" width="30" height="12"/>']
j.append(arches([-9, 0, 9], -7, 5, 10))
j.append(dome(-9, -19, 5.5, 8, 3) + dome(9, -19, 5.5, 8, 3) + dome(0, -19, 7.5, 12, 4))
j.append(f'<path d="M-4,-24 Q0,-21 4,-24 M-6,-21 Q0,-18 6,-21" fill="none" stroke="{PAPER}" stroke-width="0.7"/>')
j.append('<rect x="-21" y="-40" width="3.4" height="33"/><rect x="17.6" y="-40" width="3.4" height="33"/>')
j.append(chhatri(-19.3, -40, 5) + chhatri(19.3, -40, 5))
ICONS['jama'] = ''.join(j)

# 12 Jantar Mantar: Samrat Yantra gnomon with stair, quadrant wings
ICONS['jantar'] = (
    '<path d="M-20,0 L12,-38 L16,-38 L16,0 Z"/>'
    + ''.join(f'<line x1="{-20+i*3.2:.1f}" y1="{-i*3.8:.1f}" x2="{-17+i*3.2:.1f}" y2="{-i*3.8:.1f}" stroke="{PAPER}" stroke-width="0.7"/>' for i in range(1, 10))
    + '<path d="M-27,0 A10,10 0 0 1 -17,-10 V0 Z"/><path d="M16,0 V-10 A10,10 0 0 1 26,0 Z"/>'
    + arches([7], 0, 5, 9)
)

# 13 Safdarjung's Tomb: high arcaded platform, tall bulbous dome, corner minarets
ICONS['safdar'] = (
    '<rect x="-24" y="-11" width="48" height="11"/>'
    + arches([-18, -12, -6, 0, 6, 12, 18], 0, 4, 8)
    + '<rect x="-14" y="-27" width="28" height="16"/>'
    + arches([0], -11, 8, 13)
    + '<rect x="-7" y="-30" width="14" height="3"/>'
    + dome(0, -30, 8, 15, 4)
    + '<rect x="-17" y="-36" width="3" height="25"/><rect x="14" y="-36" width="3" height="25"/>'
    + chhatri(-15.5, -36, 4.6) + chhatri(15.5, -36, 4.6)
)

# 14 Sis Ganj Sahib: arched hall, fluted gilded dome with kalash, Nishan Sahib flag
ICONS['sisganj'] = (
    '<rect x="-17" y="-18" width="34" height="18"/>'
    + arches([-11, 0, 11], 0, 6, 12)
    + '<rect x="-7" y="-22" width="14" height="4"/>'
    + dome(0, -22, 8, 13, 5)
    + f'<path d="M-4,-25 Q-2,-31 0,-35 M4,-25 Q2,-31 0,-35" fill="none" stroke="{PAPER}" stroke-width="0.6"/>'
    + dome(-13, -18, 3.5, 5, 2) + dome(13, -18, 3.5, 5, 2)
    + '<line x1="23" y1="0" x2="23" y2="-46" stroke-width="1.3"/><path d="M23,-46 L32,-42 L23,-38 Z"/>'
)

# 15 Rashtrapati Bhavan: colonnade, drum, shallow Sanchi-like dome, chhatris
rb = ['<rect x="-30" y="-14" width="60" height="14"/>', '<rect x="-14" y="-18" width="28" height="4"/>']
rb.append(''.join(f'<line x1="{x}" y1="-2" x2="{x}" y2="-12" stroke="{PAPER}" stroke-width="1"/>' for x in range(-26, 28, 4)))
rb.append('<rect x="-9" y="-23" width="18" height="5"/>')
rb.append('<path d="M-11,-23 A11,10 0 0 1 11,-23 Z"/><rect x="-1.4" y="-36" width="2.8" height="4"/>')
rb.append(chhatri(-22, -14, 5) + chhatri(22, -14, 5))
# Jaipur Column in the forecourt, topped by lotus and star
rb.append('<rect x="34" y="-30" width="1.8" height="30"/><path d="M32.4,-30 Q34.9,-35 37.4,-30 Z"/>'
          '<path d="M34.9,-38 l1,2 h2 l-1.6,1.3 l0.6,2 l-2,-1.2 l-2,1.2 l0.6,-2 l-1.6,-1.3 h2 Z" stroke-width="0.5"/>')
ICONS['rb'] = ''.join(rb)
