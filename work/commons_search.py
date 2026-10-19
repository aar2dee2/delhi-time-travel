import json, sys, urllib.request, urllib.parse
UA = {'User-Agent': 'delhi-map-research/1.0 (personal research)'}
def q(params):
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
for term in sys.argv[1:]:
    d = q(dict(action='query', format='json', generator='search', gsrsearch=f'filetype:bitmap {term}', gsrnamespace=6, gsrlimit=25,
               prop='imageinfo', iiprop='size|url|extmetadata', iiextmetadatafilter='LicenseShortName|Artist|ObjectName'))
    print('==', term)
    rows = []
    for p in d.get('query', {}).get('pages', {}).values():
        ii = p['imageinfo'][0]; m = ii.get('extmetadata', {})
        lic = m.get('LicenseShortName', {}).get('value', '?')
        art = m.get('Artist', {}).get('value', '?')
        import re; art = re.sub('<[^>]+>', '', art)[:40]
        rows.append((ii['width'] * ii['height'], ii['width'], ii['height'], ii['size'] // 1024, lic, art, p['title']))
    for r in sorted(rows, reverse=True)[:12]:
        print(f'{r[1]}x{r[2]}  {r[3]} KB  {r[4]:<14} {r[5]:<40} {r[6]}')
