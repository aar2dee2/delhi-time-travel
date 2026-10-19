# Export the map's data (same projection, placements and fact-checked catalogue as build.py)
# and inject it into the interactive page template.
import json, sys, math
_argv = sys.argv
sys.argv = ['build.py', '/dev/null']
import build as B          # runs the static build into /dev/null; we only want its definitions
sys.argv = _argv
from icons import ICONS

STORY = {
 'lalkot': "The Tomar Rajput citadel and the first of Delhi's fortified cities. Rubble ramparts still run through the scrub west of the Qutb complex. Prithviraj Chauhan is traditionally credited with enlarging it into Qila Rai Pithora in the 12th century.",
 'qutb': "Begun by Qutb-ud-din Aibak around 1199 as a victory tower beside the Quwwat-ul-Islam mosque; Iltutmish added three storeys by about 1220. After lightning damage, Firuz Shah Tughlaq rebuilt the top (inscription dated 1369). The mosque courtyard holds the Gupta Iron Pillar, c.400 CE, brought to Delhi sometime in the 11th–13th century from a site still debated.",
 'siri': "Alauddin Khalji's walled city, built around 1303 against Mongol raids. Stretches of its round-bastioned walls survive near Shahpur Jat.",
 'tughlaq': "Ghiyas-ud-din Tughlaq's fortress capital, begun in 1321 with massive sloping walls. It was abandoned within a few years of his death in 1325.",
 'jahan': "Muhammad bin Tughlaq's “Refuge of the World”, c.1326–27: walls that joined Siri to Qila Rai Pithora and enclosed the suburbs between them. Plotted here at Bijay Mandal, a raised palace platform inside the enclosure.",
 'kotla': "The citadel of Firozabad, founded in 1354 by Firuz Shah Tughlaq on the Yamuna bank. On its pyramidal pavilion stands an Ashokan pillar of the 3rd century BCE, brought from Topra (now Yamunanagar district) around 1356. The chronicler Shams-i Siraj Afif describes the move.",
 'lodi': "A park around the tombs of the last two Sultanate dynasties: Muhammad Shah Sayyid (1444) and Sikandar Lodi (1517–18, built by his son Ibrahim), with the Bara Gumbad and Shish Gumbad between them.",
 'purana': "Humayun founded Dinpanah here in 1533. Sher Shah Suri rebuilt the fort after driving him out (c.1540–45); his Qila-i-Kuhna mosque is dated 1541. Excavations have turned up Painted Grey Ware sherds, so the mound was lived on in the 1st millennium BCE. The link to the Mahabharata's Indraprastha is tradition, not proof.",
 'humayun': "Commissioned by Humayun's widow Bega Begum (Haji Begum) and built c.1565–72 to a design by the Persian architect Mirak Mirza Ghiyas, finished by his son. The first great Mughal garden-tomb, and a UNESCO World Heritage Site.",
 'redfort': "Shah Jahan's palace-fortress for his new city of Shahjahanabad, built 1639–48 in red sandstone. A UNESCO World Heritage Site; the Prime Minister speaks from its Lahori Gate ramparts every Independence Day.",
 'jama': "Shah Jahan's congregational mosque, built 1650–56 on a rise about 0.9 km south-west of the Red Fort. One of the largest mosques in India.",
 'jantar': "One of five observatories built by Maharaja Jai Singh II of Amber, completed in 1724. Its tallest instrument, the Samrat Yantra, is a giant sundial.",
 'safdar': "Tomb of Safdarjung, wazir (chief minister) of the Mughal empire, built around 1754 by his son Shuja-ud-Daula. Often called the last monumental Mughal garden-tomb.",
 'sisganj': "Marks where the ninth Sikh Guru, Tegh Bahadur, was executed in 1675 on Aurangzeb's orders. Baghel Singh founded a shrine here in 1783; the present building dates from 1930.",
 'rb': "Built 1912–29 as the Viceroy's House to Edwin Lutyens's design; New Delhi was inaugurated in 1931. Since 1950 it has been the President of India's residence. The dome draws on the Sanchi stupa, and the Jaipur Column stands in the forecourt.",
}
OLDER = {
 'qutb': ('Iron Pillar', 400, 'c.400 CE (Gupta)', 'brought here 11th–13th c.'),
 'kotla': ('Ashokan Pillar', -250, '3rd c. BCE', 'moved from Topra c.1356'),
 'purana': ('Painted Grey Ware sherds', -800, '1st millennium BCE', 'dug up in excavations'),
}
SOURCES = {
 'lalkot': 'https://en.wikipedia.org/wiki/Lal_Kot', 'qutb': 'https://whc.unesco.org/en/list/233',
 'siri': 'https://en.wikipedia.org/wiki/Siri_Fort', 'tughlaq': 'https://en.wikipedia.org/wiki/Tughlaqabad_Fort',
 'jahan': 'https://en.wikipedia.org/wiki/Jahanpanah', 'kotla': 'https://en.wikipedia.org/wiki/Delhi-Topra_pillar',
 'lodi': 'https://en.wikipedia.org/wiki/Lodi_Gardens', 'purana': 'https://en.wikipedia.org/wiki/Purana_Qila',
 'humayun': 'https://whc.unesco.org/en/list/232', 'redfort': 'https://whc.unesco.org/en/list/231',
 'jama': 'https://en.wikipedia.org/wiki/Jama_Masjid,_Delhi', 'jantar': 'https://en.wikipedia.org/wiki/Jantar_Mantar,_New_Delhi',
 'safdar': 'https://en.wikipedia.org/wiki/Safdarjung%27s_Tomb', 'sisganj': 'https://en.wikipedia.org/wiki/Gurdwara_Sis_Ganj_Sahib',
 'rb': 'https://en.wikipedia.org/wiki/Rashtrapati_Bhavan',
}

def pts(coords, tol=1.0):
    out, last = [], None
    for lon, lat in coords:
        p = B.proj(lat, lon)
        if last is None or math.hypot(p[0]-last[0], p[1]-last[1]) >= tol:
            out.append([round(p[0], 1), round(p[1], 1)]); last = p
    p = B.proj(coords[-1][1], coords[-1][0]); out.append([round(p[0], 1), round(p[1], 1)])
    return out


from streets_data import EUROPE, STREETS, ERA_NAME
import streets_data as SD
from streetmap import make_streetmap
# one entry per catalogue row, in catalogue order, so indices match data-i in the close-up map
streets = []
for osm, old, now, who, era, link in STREETS:
    cur, line2 = SD.names(old)
    streets.append(dict(old=old, cur=cur, line2=line2, history=SD.history(old), who=who,
                        era=ERA_NAME[era], color=SD.colour(era), link=link))
streetmap_svg, label_report = make_streetmap()
missing = [k for k, v in label_report.items() if v == 'no room']
if missing: print('street labels without room:', missing, file=sys.stderr)

sites = []
for n, sid, name, built, yr, who, cent in B.SITES:
    s = B.S[sid]; x, y = B.proj(s['lat'], s['lon'])
    fd = B.R['fromDatum'].get(sid)
    sites.append(dict(n=n, id=sid, name=name, built=built, year=yr, who=who, color=B.CENT[cent][0],
                      century=B.CENT[cent][1], x=round(x, 1), y=round(y, 1), lat=s['lat'], lon=s['lon'],
                      off=B.PLACE[sid]['off'], lab=B.PLACE[sid]['lab'],
                      km=round(B.hav(B.S['rb'], s), 2), road=fd, story=STORY[sid],
                      older=OLDER.get(sid), src=SOURCES[sid], icon=ICONS[sid]))
routes = {k: dict(ids=v['ids'], km=v['km'], min=v['min'], legs=v['legs'],
                  pts=pts(v['geom'], 1.2 if k.startswith('drive') else 0.8))
          for k, v in B.R.items() if k != 'fromDatum'}
river = [pts([[g['lon'], g['lat']] for g in e['geometry']], 1.5) for e in B.Y['elements']]
data = dict(sites=sites, routes=routes, river=river, streets=streets,
            frame=dict(x0=B.MX0, y0=B.MY0, x1=B.MX1, y1=B.MY1, cx=round(B.CX, 1), cy=round(B.CY, 1), k=B.K),
            ancient=B.CENT[0][0])
tpl = open('interactive_template.html').read()
page = tpl.replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False, separators=(',', ':'))).replace('%%STREETMAP%%', streetmap_svg)
open(sys.argv[1], 'w').write(page)    # artifact version: the host adds the document skeleton
print('wrote', sys.argv[1], len(json.dumps(data)) // 1024, 'KB data')
# Standalone version for GitHub Pages: same page wrapped in a full HTML document.
head, body = page.split('<div class="wrap">', 1)
standalone = ('<!doctype html>\n<html lang="en">\n<head>\n' + head.strip() + '\n</head>\n<body>\n<div class="wrap">' + body.rstrip() + '\n</body>\n</html>\n')
import os
open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), 'index.html'), 'w').write(standalone)
print('wrote index.html (standalone)')
