# 1920s Lutyens' Delhi street names: catalogue shared by export_data.py and streetmap.py.
# ---------- Lutyens-era street names (research 17 Oct 2026) ----------
# (OSM names, 1920s name, current name / rename, namesake, era key, linked site or None)
EUROPE = '#4a5666'
STREETS = [
 (['Ashoka Road'], 'Ashoka Road', None, 'Ashoka, Maurya emperor, r. c.268–232 BCE', 0, 'kotla'),
 (['Prithviraj Road'], 'Prithviraj Road', None, 'Prithviraj Chauhan, r. c.1177–92', 12, 'lalkot'),
 (['Tughlaq Road'], 'Tughlak Road', None, 'The Tughlaq dynasty, 1320–1413', 14, 'tughlaq'),
 (['Firoz Shah Road'], 'Feroz Shah Road', None, 'Firuz Shah Tughlaq, r. 1351–88', 14, 'kotla'),
 (['Lodhi Road'], 'Lodi Road', None, 'The Lodi dynasty, 1451–1526', 15, 'lodi'),
 (['Sher Shah Road'], 'Sher Shah Road', None, 'Sher Shah Suri, r. 1540–45', 16, 'purana'),
 (['Humayun Road'], 'Humayun Road', None, 'Humayun, Mughal emperor, r. 1530–40 and 1555–56', 16, 'humayun'),
 (['Akbar Road'], 'Akbar Road', None, 'Akbar, Mughal emperor, r. 1556–1605', 16, None),
 (['Man Singh Road'], 'Man Singh Road', None, 'probably Raja Man Singh I of Amber, Akbar’s general', 16, None),
 (['Shahjahan Road'], 'Shahjahan Road', None, 'Shah Jahan, Mughal emperor, r. 1628–58', 17, 'redfort'),
 (['Doctor A.P.J. Abdul Kalam Marg', 'Doctor Avul Pakir Jainulabdeen Abdul Kalam Marg'], 'Aurangzeb Road', 'Dr APJ Abdul Kalam Road since 2015', 'Aurangzeb, Mughal emperor, r. 1658–1707', 17, 'sisganj'),
 (['Safdarjung Road'], 'Safdarjung Road', None, 'Safdarjung, Mughal wazir, d. 1754', 18, 'safdar'),
 (['Najaf Khan Road'], 'Najaf Khan Road', None, 'Mirza Najaf Khan, Mughal commander, d. 1782', 18, None),
 (['Jai Singh Road'], 'Jai Singh Road', None, 'Jai Singh of Amber (sources differ on whether I or II)', None, None),
 (['Kartavya Path'], 'Kingsway', 'Rajpath after Independence (1955), Kartavya Path 2022', 'King George V', 'eu', 'rb'),
 (['Janpath'], 'Queensway', 'Janpath after Independence (1955)', 'the Queen (often said to be Queen Mary; unverified)', 'eu', None),
 (['Kasturba Gandhi Marg'], 'Curzon Road', 'Kasturba Gandhi Marg', 'Lord Curzon, Viceroy 1899–1905', 'eu', None),
 (['Tilak Marg'], 'Hardinge Avenue', 'Tilak Marg', 'Lord Hardinge, Viceroy 1910–16', 'eu', None),
 (['Baba Kharak Singh Marg'], 'Irwin Road', 'Baba Kharak Singh Marg', 'Lord Irwin, Viceroy 1926–31', 'eu', None),
 (['Mandir Marg'], 'Reading Road', 'Mandir Marg', 'Lord Reading, Viceroy 1921–26', 'eu', None),
 (['Copernicus Marg'], 'Lytton Road', 'Copernicus Marg', 'Lord Lytton, Viceroy 1876–80', 'eu', None),
 (['Dr. Zakir Hussain Marg', 'Doctor Zakir Hussain Marg'], 'Wellesley Road', 'Dr Zakir Hussain Marg', 'Lord Wellesley, Governor-General 1798–1805', 'eu', None),
 (['Krishna Menon Marg'], 'Hastings Road', 'Krishna Menon Marg', 'Warren Hastings, Governor-General 1773–85', 'eu', None),
 (['Subramaniyam Bharti Marg'], 'Cornwallis Road', 'Subramania Bharti Marg', 'Lord Cornwallis, Governor-General 1786–93', 'eu', None),
 (['Dara Shikoh Road'], 'Dalhousie Road', 'Dara Shikoh Road since 2017', 'Lord Dalhousie, Governor-General 1848–56', 'eu', None),
 (['Tyagaraj Marg'], 'Clive Road', 'Thyagaraja Marg', 'Robert Clive', 'eu', None),
 (['Kumaraswami Kamaraj Marg'], 'Dupleix Road', 'Kamaraj Marg', 'Joseph-François Dupleix, French governor', 'eu', None),
 (['Tees January Road'], 'Albuquerque Road', 'Tees January Marg', 'Afonso de Albuquerque, Portuguese governor', 'eu', None),
 (['Sardar Patel Marg'], 'Kitchener Road', 'Sardar Patel Marg', 'Lord Kitchener, Commander-in-Chief', 'eu', None),
 (['Mother Teresa Crescent'], 'Willingdon Crescent', 'Mother Teresa Crescent', 'Lord Willingdon, Viceroy 1931–36 (so named in the 1930s, not the 1920s)', 'eu', None),
 (['Motilal Nehru Marg'], 'York Road', 'Motilal Nehru Marg', 'probably Prince Albert, Duke of York (later George VI); sources thin', 'eu', None),
 (['Rajaji Marg'], 'King George’s Avenue', 'Rajaji Marg', 'King George (V or VI; sources differ)', 'eu', None),
 (['Maulana Azad Road'], 'King Edward Road', 'Maulana Azad Road', 'King Edward VII', 'eu', None),
]
ERA_NAME = {0: 'Ancient', 12: 'Rajput', 14: 'Delhi Sultanate', 15: 'Delhi Sultanate', 16: 'Sur & Mughal', 17: 'Mughal', 18: 'Late Mughal', None: 'Uncertain', 'eu': 'British & European'}

# Lok Kalyan Marg is not a ruler's or viceroy's name, but it is the best-known renaming in the area since 2014.
STREETS.append((['Lok Kalyan Marg'], 'Race Course Road', 'Lok Kalyan Marg since 2016', 'the Delhi race course (Delhi Race Club, founded here 1926, registered 1940; not a ruler)', 'other', None))
# OSM still labels this lane with its old name; NDMC renamed it in June 2023.
STREETS.append((['Aurangzeb Lane'], 'Aurangzeb Lane', 'Dr APJ Abdul Kalam Lane since 2023', 'Aurangzeb, Mughal emperor, r. 1658–1707', 17, 'sisganj'))
ERA_NAME['other'] = 'Other renaming since 2014'

ERA_COLOUR = {0: '#3d3566', 12: '#2f7480', 14: '#3d8a6e', 15: '#7d9a3c', 16: '#c49a1e', 17: '#d07a2a',
              18: '#b8432e', None: '#8d7fae', 'eu': EUROPE, 'other': '#a08a6a'}
def colour(era): return ERA_COLOUR[era]

# Names over time, keyed by the 1920s name: (current name, name until it changed after 2014, year changed).
# Roads renamed between Independence and 2014 have a single later name, so the middle field is None.
NAMES = {
    'Kingsway': ('Kartavya Path', 'Rajpath', 2022),
    'Aurangzeb Road': ('Dr APJ Abdul Kalam Road', 'Aurangzeb Road', 2015),
    'Aurangzeb Lane': ('Dr APJ Abdul Kalam Lane', 'Aurangzeb Lane', 2023),
    'Dalhousie Road': ('Dara Shikoh Road', 'Dalhousie Road', 2017),
    'Race Course Road': ('Lok Kalyan Marg', 'Race Course Road', 2016),
    'Queensway': ('Janpath', None, None),
    'Curzon Road': ('Kasturba Gandhi Marg', None, None),
    'Hardinge Avenue': ('Tilak Marg', None, None),
    'Irwin Road': ('Baba Kharak Singh Marg', None, None),
    'Reading Road': ('Mandir Marg', None, None),
    'Lytton Road': ('Copernicus Marg', None, None),
    'Wellesley Road': ('Dr Zakir Hussain Marg', None, None),
    'Hastings Road': ('Krishna Menon Marg', None, None),
    'Cornwallis Road': ('Subramania Bharti Marg', None, None),
    'Clive Road': ('Tyagraj Marg', None, None),
    'Dupleix Road': ('Kamaraj Marg', None, None),
    'Albuquerque Road': ('Tees January Marg', None, None),
    'Kitchener Road': ('Sardar Patel Marg', None, None),
    'Willingdon Crescent': ('Mother Teresa Crescent', None, None),
    'York Road': ('Motilal Nehru Marg', None, None),
    'King George’s Avenue': ('Rajaji Marg', None, None),
    'King Edward Road': ('Maulana Azad Road', None, None),
    # spelling variants only, not renamings: official signs and maps differ, so no bracket is needed
    'Tughlak Road': ('Tughlak Road', None, None),
    'Feroz Shah Road': ('Feroz Shah Road', None, None),
    'Lodi Road': ('Lodhi Road', None, None),
}
ALSO_SPELLED = {'Tughlak Road': 'Tughlaq Road', 'Feroz Shah Road': 'Firoz Shah Road or Ferozshah Road', 'Lodi Road': 'Lodi Road'}
SPELLING_ONLY = {'Tughlak Road', 'Feroz Shah Road', 'Lodi Road'}

def names(old):
    """Map label lines: current name, and the older name(s) in brackets (None if unchanged)."""
    cur, pre, year = NAMES.get(old, (old, None, None))
    if pre and pre != old:                         # e.g. Kingsway -> Rajpath -> Kartavya Path
        return cur, f'({pre} until {year} · {old} in the 1920s)'
    if pre:                                        # renamed after 2014, 1920s name kept until then
        return cur, f'({old} until {year})'
    if cur != old and old not in SPELLING_ONLY:
        return cur, f'({old})'
    return cur, None

def history(old):
    """One-line history for the list and tooltips."""
    cur, pre, year = NAMES.get(old, (old, None, None))
    if old == 'Race Course Road':
        return 'Race Course Road until 2016 (when it got that name is not established)'
    if old == 'Willingdon Crescent':
        return 'Willingdon Crescent from the 1930s; renamed Mother Teresa Crescent by the NDMC on 26 September 2003'
    if old == 'Aurangzeb Lane':
        return 'Aurangzeb Lane until June 2023'
    if pre and pre != old:
        return f'{old} in the 1920s, {pre} after Independence, {cur} since {year}'
    if pre:
        return f'{old} from the 1920s until {year}' if old != 'Aurangzeb Lane' else f'{old} until {year}'
    if cur != old and old not in SPELLING_ONLY:
        return f'{old} in the 1920s; renamed after Independence'
    if old in SPELLING_ONLY:
        return f'Unchanged; also spelled {ALSO_SPELLED[old]}'
    return 'Unchanged since the 1920s'
