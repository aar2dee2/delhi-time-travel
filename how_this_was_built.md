# How to Time Travel in Delhi: How This Was Built

Fifteen monuments founded over about nine centuries stand within about 13 km of Raisina Hill. This file records how the map was made, what was checked, and where each fact comes from. It is the single notes file for the project. Last updated 19 October 2026.

## What's in the project

- `delhi_deep_time_map.svg`: the static map, with the "how far you go, how far back you get" chart, the key and the suggested day.
- `index.html`: the interactive version, with a time dial, the 1920s street-name layer and the double-dome thread. It is published with GitHub Pages at https://aar2dee2.github.io/delhi-time-travel/.
- `time_travel_delhi.html`: the same page without the HTML document wrapper, as used for the Claude artifact.
- `blog/`: images for the blog post (map only; the full poster at 2400 px and 4800 px), plus `blog/domes/` with photo + cutaway comparisons for each dome.
- `work/`: the scripts and data that generate everything above. Run `build.py` for the static map, `export_data.py` for both versions of the interactive page, `blog_images.py` for the blog images, and `dome_compare.py` for the dome comparisons. The original dome photos aren't in the repo. To rebuild the comparisons, download the four files listed in `work/photo_credits.json` into `photos_dl/` as lodi.jpg, humayun.jpg, rb.jpg and florence.jpg.

## Method

- **Coordinates.** The original ten sites keep their first-draft coordinates. New sites come from OpenStreetMap: Lal Kot (castle feature), Siri (castle feature), Jahanpanah at Bijay Mandal. Jantar Mantar and Jama Masjid come from Wikipedia.
- **Projection.** Local equirectangular, centred on Raisina Hill, north up, 44 px per km.
- **Rings.** Straight-line distance every 3 km. Each ring is about 40 minutes' walk at 4.5 km/h.
- **Routes and times.** Real road and footpath routing from OpenStreetMap, using the FOSSGIS OSRM servers. Drive times are *free-flow*, so expect Delhi traffic to make them 2–3× longer. Walk times are realistic.
- **Distance vs. age chart.** A least-squares fit of start year against straight-line km gives about 55 years back per km (r = −0.77). It's a rule of thumb, not a law: the Mughal north breaks it.
- **Colour.** Colour shows the century each site was founded (Sis Ganj is coloured for its 1783 founding, though the present building is 1930). Indigo marks objects older than the site they stand in.
- **Not fact-checked yet:** the Rashtrapati Bhavan Circuit 1 tour guide. The map uses only two of its details: the Sanchi-style dome and the Jaipur Column.


## Dates printed on the map

| # | Site | Printed | Verdict and notes | Sources |
|---|---|---|---|---|
| 1 | Lal Kot | c.1060 | Correct. Built by Anangpal II Tomar, c.1052–60. Prithviraj Chauhan is usually credited with enlarging it into Qila Rai Pithora (12th c.), but excavators call that attribution only "possible". | [Lal Kot](https://en.wikipedia.org/wiki/Lal_Kot) |
| 2 | Qutb Minar | c.1199–1220 | Corrected. 1199 is the best start date; 1192 is the conquest year. Aibak built storey 1 and Iltutmish storeys 2–4. Firuz Shah rebuilt the top after lightning (inscription dated 1369), and Sikandar Lodi repaired it in 1503. Wikipedia's "1199–1503" mixes construction with repair. | [UNESCO 233](https://whc.unesco.org/en/list/233), [Qutb Minar](https://en.wikipedia.org/wiki/Qutb_Minar) |
| 2a | Iron Pillar | c.400 CE | Correct with caveats. Gupta, attributed to Chandragupta II (r. c.375–415); weighs more than 6 tonnes. Its original site is unknown: Udayagiri, Mathura and Vidisha have all been proposed. It was brought to Delhi sometime in the 11th–13th c., and who moved it is debated. | [Iron pillar](https://en.wikipedia.org/wiki/Iron_pillar_of_Delhi) |
| 3 | Siri | c.1303 | Correct. Built by Alauddin Khalji against Mongol raids. | [Siri Fort](https://en.wikipedia.org/wiki/Siri_Fort) |
| 4 | Tughlaqabad | 1321–c.1325 | Correct. Begun 1321, abandoned by c.1327. | [Tughlaqabad](https://en.wikipedia.org/wiki/Tughlaqabad_Fort) |
| 5 | Jahanpanah | c.1326–27 | Correct. Muhammad bin Tughlaq's walls linked Siri and Qila Rai Pithora. Plotted at Bijay Mandal, his palace inside the enclosure. | [Jahanpanah](https://en.wikipedia.org/wiki/Jahanpanah) |
| 6 | Feroz Shah Kotla | 1354 | Correct. | [Delhi SRDC](https://srdc.delhi.gov.in/en/srdc/1300-1400) |
| 6a | Ashokan Pillar | 3rd c. BCE | Correct. Topra Kalan is now in **Yamunanagar** district, not Ambala. Re-erected c.1356. Shams-i Siraj Afif describes the move. | [Delhi-Topra pillar](https://en.wikipedia.org/wiki/Delhi-Topra_pillar) |
| 7 | Lodi Gardens | 1444–1518 | Correct. Muhammad Shah Sayyid's tomb dates to 1444; Sikandar Lodi's tomb to 1517–18, built by Ibrahim Lodi. Lodi now shares the Sultanate period in the colour scheme. | [Lodi Gardens](https://en.wikipedia.org/wiki/Lodi_Gardens) |
| 8 | Purana Qila | 1533–c.1545 | Corrected. Humayun founded Dinpanah in 1533 (Wikipedia's infobox gives 1538). Sher Shah rebuilt it c.1540–45, and his mosque is dated 1541. | [Purana Qila](https://en.wikipedia.org/wiki/Purana_Qila) |
| 8a | Painted Grey Ware | "1st millennium BCE" | **Softened.** PGW comes from stray sherds, some found in Mauryan levels, and excavators have not reached natural soil. "~1000 BCE" (older literature) and "~900 BCE" (ASI) are claims, not settled facts. B.B. Lal dug in 1954–55 and 1969–73; Swarnkar ran three seasons (2013–14, 2017–18, 2022–23). The Indraprastha link is traditional only. | [Daily Pioneer 2023](https://www.dailypioneer.com/2023/page1/purana-qila-reveals-more-of-its-historic-past.html) |
| 9 | Humayun's Tomb | 1565–72 | Contested start. Sources disagree on the commissioning date (1558 or 1565); construction 1565–72 is the most widely cited span. Built by Bega (Haji) Begum, with Mirak Mirza Ghiyas as architect and his son Sayyid Muhammad completing it. Some websites say it was begun "nine days" after Humayun's death; it was about nine *years* (he died in 1556). | [UNESCO 232](https://whc.unesco.org/en/list/232) |
| 10 | Red Fort | 1639–48 | Correct. | [UNESCO 231](https://whc.unesco.org/en/list/231) |
| 11 | Jama Masjid | 1650–56 | Correct. It lies about 0.9 km **SW** of the Red Fort, not "just west". | [Jama Masjid](https://en.wikipedia.org/wiki/Jama_Masjid,_Delhi) |
| 12 | Jantar Mantar | 1724 | Correct. Work began in 1723. A plaque giving 1710 is considered wrong. | [Jantar Mantar](https://en.wikipedia.org/wiki/Jantar_Mantar,_New_Delhi) |
| 13 | Safdarjung's Tomb | c.1754 | Corrected. Safdarjung died in 1754 and the inscription is dated 1754, so the "1753–54" printed by ASI and others is doubtful. Change "last Mughal garden-tomb" to "often called the last". | [Safdarjung's Tomb](https://en.wikipedia.org/wiki/Safdarjung%27s_Tomb) |
| 14 | Sis Ganj Sahib | 1783 · bldg 1930 | Clarified. The martyrdom was in 1675 and Baghel Singh founded the shrine in 1783. The present building dates from **1930**, with gilding and expansion after 1971. | [Sis Ganj](https://en.wikipedia.org/wiki/Gurdwara_Sis_Ganj_Sahib) |
| 15 | Rashtrapati Bhavan | 1912–29 | Correct. Announced 12 Dec 1911, built 1912–29, New Delhi inaugurated 13 Feb 1931. Lutyens designed the house; Herbert Baker designed the Secretariats. | [Rashtrapati Bhavan](https://en.wikipedia.org/wiki/Rashtrapati_Bhavan) |


## Other claims

- **Seven cities.** The list is the commonly cited one. Variants add Indraprastha, split Lal Kot from Qila Rai Pithora, use Shergarh for Dinpanah, or add Kilokhri, Adilabad, Mubarakabad and others, so some counts reach "eleven or more".
- **Isochronic maps.** Galton's 1881 chart and Bartholomew's 1914 *Atlas of Economic Geography* are both confirmed, so the Bartholomew attribution moves up from moderate to high confidence. Bartholomew also used the idea earlier, in 1889.
- **Bearings.** Old Delhi lies 35–41° from Raisina, which is NE. The v1 prose called it NNE.


## Lutyens' Delhi street names

**Claim checked:** the roads radiating around India Gate and Rashtrapati Bhavan were named after different periods of history.

- **Documented (high confidence):** many 1920s New Delhi avenues were deliberately named after earlier rulers of India: Ashoka, Prithviraj, the Tughlaqs, Firuz Shah, the Lodis, Sher Shah, Humayun, Akbar, Shahjahan, Aurangzeb and Safdarjung. The rest were named after viceroys and other Europeans who ruled parts of India (Curzon, Hardinge, Irwin, Clive, Dupleix, Albuquerque and others). Narayani Gupta cites Percival Spear's 1943 book, in which Spear says he was asked to suggest names from Indian history. ([The Wire](https://cms.thewire.in/news/history-needs-informed-debate-not-the-erasure-of-aurangzeb-to-install-kalam))
- **Interpretation (moderate confidence):** that the names presented the Raj as the latest heir to Delhi's empires. Swapna Liddle calls it a "rebranding" ([ThePrint](https://theprint.in/feature/around-town/british-gave-delhi-a-makeover-to-show-they-werent-all-bad-ended-up-with-lutyens-baker-ego-war/2277615/)), but no official statement of that motive has been found.
- **Not supported:** zoning by period. Mughal, Sultanate and viceregal names are mixed together. Tughlak Road is about 11 km from Tughlaqabad as the crow flies. No road for Jahangir or the Khaljis has been found; this is inferred from present-day names, not from a 1920s list.
- **Renamings verified:**
  - Kingsway → Rajpath (after Independence, 1955) → Kartavya Path (2022)
  - Aurangzeb Road → Dr APJ Abdul Kalam Road (2015)
  - Race Course Road → Lok Kalyan Marg (2016)
  - Dalhousie Road → Dara Shikoh Road (2017)

  The other old-to-new pairs for viceregal roads follow the Wikipedia and Delhi Walla lists. The namesakes of Queensway, York Road and King George's Avenue are thinly sourced.
- **Not Lutyens-era:** Chandragupta Marg and Kautilya Marg (Chanakyapuri, 1950s). They are not on the map.

**What's documented, what's interpretation, what doesn't hold up** (this summary used to sit on the interactive page):
- **Documented:** the deliberate roll-call of rulers across eras.
- **Interpretation:** that it was meant to present the Raj as the latest heir to Delhi's empires. It's a common reading, but no official statement of that motive has been found.
- **Doesn't hold up:** neat zoning by period. Mughal, Sultanate and viceregal names are mixed together, and some sit far from their namesake's monuments (Tughlak Road is about 11 km from Tughlaqabad as the crow flies). No road was named after Jahangir or the Khaljis.
- **Caveat:** street names come from OpenStreetMap. Old-to-new pairings for viceregal roads follow published lists and are less certain than the rulers' names.


## Double domes

**Claims on the interactive page and the comparison images:**
- **Sikandar Lodi's tomb (1517–18):** often cited as India's first double dome. Some sources call it only a first step, and an earlier tomb in Srinagar (c.1465) has also been proposed. ([GKToday](https://www.gktoday.in/double-dome/), [Archnet](https://www.archnet.org/sites/1585))
- **Humayun's Tomb (c.1565–72):** generally credited with the first fully developed Persian-style double dome in India. Its architect, Mirak Mirza Ghiyas, had worked in Herat and Bukhara. ([University of Washington Silk Road project](https://depts.washington.edu/silkroad/cities/india/delhi/humayun/humayun.html))
- **Rashtrapati Bhavan (1912–29):** the official site describes "a lower dome beneath this main dome". The main dome is copper-clad and about 55 m above the forecourt; its outer form is said to draw on the Sanchi stupa. Construction details of the inner dome weren't found. ([President of India](https://www.presidentofindia.gov.in/hi/node/1129), [Rashtrapati Bhavan](https://rashtrapatibhavan.gov.in/rbtour/central-dome))
- **Florence (1420–36):** earlier than Humayun's Tomb but a separate tradition. The double shell and the stone-and-timber chains were already specified in Neri di Fioravanti's 1367 design. Brunelleschi's breakthrough was building it without timber centring, using herringbone brickwork, a pointed ("quinto acuto") profile and new hoists. The thick inner shell carries the load. The theory that Persian domes such as Soltaniyeh influenced Florence (Sanpaolesi, 1972) is real but contested. ([Museo Galileo](https://brunelleschi.imss.fi.it/itineraries/place/TheDomeOfSantaMariaFiore.html), [Dome of Soltaniyeh](https://en.wikipedia.org/wiki/Dome_of_Soltaniyeh))

**Brunelleschi fact-check (Fable, 19 Oct 2026).** Two errors in the first answer were corrected:
- Foundation to finished dome was about **140 years** (1296 to 1436), not 120.
- The double shell wasn't Brunelleschi's invention. Persian double domes were also structural, not just about the skyline.

Nuances: there was no clean winner of the 1418 competition (his scheme was adopted in 1420 with Ghiberti as co-supervisor, and he took sole charge around 1423). The "Gothic and foreign buttresses" motive comes largely from Ross King's narrative. The ball's date is given as 1466, 1469 or 1471. A 1970s survey found no trace of the iron chains.

**The cutaways are schematic.** They show how the shells relate, not measured profiles.

## Photo credits (dome comparison images)

| Dome | Photographer | File (Wikimedia Commons) | Licence |
|---|---|---|---|
| Sikandar Lodi's tomb | Pinakpani | [Tomb of Sikandar Lodi in Lodi Garden 09.jpg](https://commons.wikimedia.org/wiki/File:Tomb_of_Sikandar_Lodi_in_Lodi_Garden_09.jpg) | CC BY-SA 4.0 |
| Humayun's Tomb | Harsh7284 | [Humayun's Tomb Front Mighty.jpg](https://commons.wikimedia.org/wiki/File:Humayun%27s_Tomb_Front_Mighty.jpg) | CC BY-SA 4.0 |
| Rashtrapati Bhavan | Baap8969 | [Rashtrapati Bhavan in New Delhi.jpg](https://commons.wikimedia.org/wiki/File:Rashtrapati_Bhavan_in_New_Delhi.jpg) | CC0 |
| Florence Cathedral | Angela Stefanoni | [Cupola del Brunelleschi - panoramio.jpg](https://commons.wikimedia.org/wiki/File:Cupola_del_Brunelleschi_-_panoramio.jpg) | CC BY 3.0 |

The Lodi and Humayun comparison images combine CC BY-SA photos, so they are shared under CC BY-SA 4.0. Credits are printed on every image.

## Corrections from the first draft

- Humayun's Tomb is printed as 1565–72; the commissioning date is disputed (1558 or 1565).
- Purana Qila is dated from its 1533 founding, and the PGW sherds are shown as "1st millennium BCE", not a hard 1000 BCE.
- Safdarjung's Tomb is c.1754 (after his death), not 1753.
- The Sis Ganj building is dated 1930.
- Qutb Minar is c.1199–1220, with the top storeys rebuilt in 1369.
- Topra is in Yamunanagar district.
- Jama Masjid lies SW of the Red Fort, not W.
- Old Delhi's bearings from Raisina are NE (35–41°), not NNE.
- Era colours were replaced by century colours, and Lodi is now treated as Sultanate.

## Limitations

- **Survivorship bias.** This is a map of what power built in stone. The houses and bazaars of every century shown are almost all gone.
- **The 19th century is missing.** The century of 1857 has no monument on the map. This is the most visible gap, and a candidate for a future layer.
- **Drive times are free-flow.** They come from OpenStreetMap routing; expect 2–3× longer in Delhi traffic.

## Independent audit (Fable, 17 Oct 2026)

**Confirmed:** every monument date, all coordinates (within 0.1–0.4 km of independent geotags), distances, the fit (55 years/km, r = −0.77), route totals, and consistency across the map, the page and these notes.

**Fixed after the audit:**
- BCE years were off by one on the time dial.
- The page was missing its mobile viewport setting.
- "Tughlak Road 15 km" corrected to about 11 km straight-line.
- Uncertain namesakes are now hedged.
- Tughlaq dynasty end date corrected to 1413.
- The colour legend now says "century founded".
- The PGW range now spans the whole 1st millennium BCE.
- Keyboard access added to the street list and itinerary.
- The screen-reader announcement no longer fires on every frame of the animation.
