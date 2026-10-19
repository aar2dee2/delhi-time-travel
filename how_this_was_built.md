# How to Time Travel in Delhi: How This Was Built

Fifteen monuments founded over about nine centuries stand within about 13 km of Raisina Hill. This file records how the map was made, what was checked, and where each fact comes from. It is the single notes file for the project. Last updated 19 October 2026.

## What's in the project

- `delhi_deep_time_map.svg`: the static map, with the "how far you go, how far back you get" chart, the key and the suggested day.
- `index.html`: the interactive version, with a time dial, a close-up street map of Lutyens' Delhi and the double-dome thread. It is published with GitHub Pages at https://aar2dee2.github.io/delhi-time-travel/.
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

Numbers follow the suggested route, starting at 0 (Rashtrapati Bhavan, the map's centre).

| # | Site | Printed | Verdict and notes | Sources |
|---|---|---|---|---|
| 0 | Rashtrapati Bhavan | 1912–29 | Correct. Announced 12 Dec 1911, built 1912–29, New Delhi inaugurated 13 Feb 1931. Lutyens designed the house; Herbert Baker designed the Secretariats. | [Rashtrapati Bhavan](https://en.wikipedia.org/wiki/Rashtrapati_Bhavan) |
| 1 | Jantar Mantar | 1724 | Correct. Work began in 1723. A plaque giving 1710 is considered wrong. | [Jantar Mantar](https://en.wikipedia.org/wiki/Jantar_Mantar,_New_Delhi) |
| 2 | Sis Ganj Sahib | 1783 · bldg 1930 | Clarified. The martyrdom was in 1675 and Baghel Singh founded the shrine in 1783. The present building dates from **1930**, with gilding and expansion after 1971. | [Sis Ganj](https://en.wikipedia.org/wiki/Gurdwara_Sis_Ganj_Sahib) |
| 3 | Red Fort | 1639–48 | Correct. | [UNESCO 231](https://whc.unesco.org/en/list/231) |
| 4 | Jama Masjid | 1650–56 | Correct. It lies about 0.9 km **SW** of the Red Fort, not "just west". | [Jama Masjid](https://en.wikipedia.org/wiki/Jama_Masjid,_Delhi) |
| 5 | Feroz Shah Kotla | 1354 | Correct. | [Delhi SRDC](https://srdc.delhi.gov.in/en/srdc/1300-1400) |
| 5a | Ashokan Pillar | 3rd c. BCE | Correct. Topra Kalan is now in **Yamunanagar** district, not Ambala. Re-erected c.1356. Shams-i Siraj Afif describes the move. | [Delhi-Topra pillar](https://en.wikipedia.org/wiki/Delhi-Topra_pillar) |
| 6 | Purana Qila | 1533–c.1545 | Corrected. Humayun founded Dinpanah in 1533 (Wikipedia's infobox gives 1538). Sher Shah rebuilt it c.1540–45, and his mosque is dated 1541. | [Purana Qila](https://en.wikipedia.org/wiki/Purana_Qila) |
| 6a | Painted Grey Ware | "1st millennium BCE" | **Softened.** PGW comes from stray sherds, some found in Mauryan levels, and excavators have not reached natural soil. "~1000 BCE" (older literature) and "~900 BCE" (ASI) are claims, not settled facts. B.B. Lal dug in 1954–55 and 1969–73; Swarnkar ran three seasons (2013–14, 2017–18, 2022–23). The Indraprastha link is traditional only. | [Daily Pioneer 2023](https://www.dailypioneer.com/2023/page1/purana-qila-reveals-more-of-its-historic-past.html) |
| 7 | Humayun's Tomb | 1565–72 | Contested start. Sources disagree on the commissioning date (1558 or 1565); construction 1565–72 is the most widely cited span (ASI, UNESCO). Lowry (Muqarnas 4, 1987), citing Badauni, gives 1562–71, with completion in 1572. Built by Bega (Haji) Begum, with Mirak Mirza Ghiyas as architect and his son Sayyid Muhammad completing it. Some websites say it was begun "nine days" after Humayun's death; it was about nine *years* (he died in 1556). | [UNESCO 232](https://whc.unesco.org/en/list/232) |
| 8 | Lodi Gardens | 1444–1518 | Correct. Muhammad Shah Sayyid's tomb dates to 1444; Sikandar Lodi's tomb to 1517–18, built by Ibrahim Lodi. Lodi now shares the Sultanate period in the colour scheme. | [Lodi Gardens](https://en.wikipedia.org/wiki/Lodi_Gardens) |
| 9 | Safdarjung's Tomb | c.1754 | Corrected. Safdarjung died in 1754 and the inscription is dated 1754, so the "1753–54" printed by ASI and others is doubtful. Change "last Mughal garden-tomb" to "often called the last". | [Safdarjung's Tomb](https://en.wikipedia.org/wiki/Safdarjung%27s_Tomb) |
| 10 | Siri | c.1303 | Correct. Built by Alauddin Khalji against Mongol raids. | [Siri Fort](https://en.wikipedia.org/wiki/Siri_Fort) |
| 11 | Tughlaqabad | 1321–c.1325 | Correct. Begun 1321, abandoned by c.1327. | [Tughlaqabad](https://en.wikipedia.org/wiki/Tughlaqabad_Fort) |
| 12 | Jahanpanah | c.1326–27 | Correct. Muhammad bin Tughlaq's walls linked Siri and Qila Rai Pithora. Plotted at Bijay Mandal, his palace inside the enclosure. | [Jahanpanah](https://en.wikipedia.org/wiki/Jahanpanah) |
| 13 | Qutb Minar | c.1199–1220 | Corrected. 1199 is the best start date; 1192 is the conquest year. Aibak built storey 1 and Iltutmish storeys 2–4. Firuz Shah rebuilt the top after lightning (inscription dated 1369), and Sikandar Lodi repaired it in 1503. Wikipedia's "1199–1503" mixes construction with repair. | [UNESCO 233](https://whc.unesco.org/en/list/233), [Qutb Minar](https://en.wikipedia.org/wiki/Qutb_Minar) |
| 13a | Iron Pillar | c.400 CE | Correct with caveats. Gupta, attributed to Chandragupta II (r. c.375–415); weighs more than 6 tonnes. Its original site is unknown: Udayagiri, Mathura and Vidisha have all been proposed. It was brought to Delhi sometime in the 11th–13th c., and who moved it is debated. | [Iron pillar](https://en.wikipedia.org/wiki/Iron_pillar_of_Delhi) |
| 14 | Lal Kot | c.1060 | Correct. Built by Anangpal II Tomar, c.1052–60. Prithviraj Chauhan is usually credited with enlarging it into Qila Rai Pithora (12th c.), but excavators call that attribution only "possible". | [Lal Kot](https://en.wikipedia.org/wiki/Lal_Kot) |


## Other claims

- **Seven cities.** The list is the commonly cited one. Variants add Indraprastha, split Lal Kot from Qila Rai Pithora, use Shergarh for Dinpanah, or add Kilokhri, Adilabad, Mubarakabad and others, so some counts reach "eleven or more".
- **Isochronic maps.** Galton's 1881 chart and Bartholomew's 1914 *Atlas of Economic Geography* are both confirmed, so the Bartholomew attribution moves up from moderate to high confidence. Bartholomew also used the idea earlier, in 1889.
- **Bearings.** Old Delhi lies 35–41° from Raisina, which is NE. The v1 prose called it NNE.


## Lutyens' Delhi street names

**Claim checked:** the roads radiating around India Gate and Rashtrapati Bhavan were named after different periods of history.

- **Documented (high confidence):** many 1920s New Delhi avenues were deliberately named after earlier rulers of India: Ashoka, Prithviraj, the Tughlaqs, Firuz Shah, the Lodis, Sher Shah, Humayun, Akbar, Shahjahan, Aurangzeb and Safdarjung. The rest were named after viceroys and other Europeans who ruled parts of India (Curzon, Hardinge, Irwin, Clive, Dupleix, Albuquerque and others). Narayani Gupta writes that Percival Spear, who drew attention to the historical street names in his 1943 book Delhi: Its Monuments and History, had himself been asked to suggest names from Indian history. ([The Wire](https://cms.thewire.in/news/history-needs-informed-debate-not-the-erasure-of-aurangzeb-to-install-kalam))
- **Interpretation (moderate confidence):** that the names presented the Raj as the latest heir to Delhi's empires. Swapna Liddle calls it a "rebranding" ([ThePrint](https://theprint.in/feature/around-town/british-gave-delhi-a-makeover-to-show-they-werent-all-bad-ended-up-with-lutyens-baker-ego-war/2277615/)), but no official statement of that motive has been found.
- **Not supported:** zoning by period. Mughal, Sultanate and viceregal names are mixed together. Tughlak Road is about 11 km from Tughlaqabad as the crow flies. No road for Jahangir or the Khaljis has been found; this is inferred from present-day names, not from a 1920s list.
- **Renamings since 2014, verified (all decided by the NDMC):**
  - Aurangzeb Road → Dr APJ Abdul Kalam Road (28 Aug 2015)
  - Race Course Road → Lok Kalyan Marg (21 Sep 2016)
  - Dalhousie Road → Dara Shikoh Road (6 Feb 2017)
  - Rajpath → Kartavya Path (7 Sep 2022). Kingsway became Rajpath, and Queensway Janpath, after Independence. Nehru's note of 24 July 1955 proposed exactly these names as a first, limited batch, so 1955 is the likely date, but no formal decision record has been found.
  - Aurangzeb Lane → Dr APJ Abdul Kalam Lane (June 2023). OpenStreetMap still uses the old name, so the map labels it from this list.
- **Not official renamings:** Teen Murti Chowk became Teen Murti Haifa Chowk in 2018, but it's a roundabout, not a road. In March 2025 two MPs put "Swami Vivekananda Marg" on their Tughlak Lane nameplates, and later that month activists spray-painted other names over the signs for Shahjahan Road, Akbar Road, Humayun Road and Tughlak Lane; neither led to an NDMC decision. No NDMC road renamings in the area were found for 2024–26.
- **Dates and namesakes with caveats:**
  - **Willingdon Crescent:** Willingdon was Viceroy only from 1931, so the crescent was named in the 1930s, not the 1920s. The NDMC resolved to rename it Mother Teresa Crescent at its meeting of 26 September 2003 (minutes confirmed 31 October 2003).
  - **Race Course Road:** when it got that name isn't established. The Delhi Race Club was founded at this site in 1926 and registered in 1940.
  - **Tees January Marg:** Nehru's note of 24 July 1955 proposed the name for Albuquerque Road. Popular accounts say 1948 (unverified).
  - **Unsourced namesakes and pairs:** Queensway's namesake (often said to be Queen Mary; unverified), Man Singh Road (probably Man Singh I), Jai Singh Road (I or II) and York Road (probably Prince Albert, Duke of York) are not documented. The Wellesley Road → Dr Zakir Hussain Marg and Hastings Road → Krishna Menon Marg pairs rest on general lists. Tilak Marg's old name is given as Hardinge Avenue by the Delhi Walla and as Hardinge Road by Wikipedia.
- **Spelling variants, not renamings:** Tughlak Road (also spelled Tughlaq), Feroz Shah Road (also Firoz Shah or Ferozshah) and Lodhi Road (also Lodi). Clive Road is now Tyagraj Marg, the NDMC spelling; Thyagaraja Marg is also used.

  The other old-to-new pairs for viceregal roads follow the Wikipedia and Delhi Walla lists.
- **The close-up street map** shows every major road in grey, from OpenStreetMap. Roads named after rulers or colonial officials are coloured by the namesake's era. Labels give today's name, with older names in brackets. Where a road was renamed after 2014, the bracket gives the name it had until then and the year it changed. New Delhi's plan is not concentric circles: Lutyens laid it out as hexagons and triangles, with avenues radiating from roundabouts such as India Gate's hexagon and Connaught Place's rings.
- **Not Lutyens-era:** Chandragupta Marg and Kautilya Marg (Chanakyapuri, 1950s). They are not on the map.

**What's documented, what's interpretation, what doesn't hold up** (this summary used to sit on the interactive page):
- **Documented:** the deliberate roll-call of rulers across eras.
- **Interpretation:** that it was meant to present the Raj as the latest heir to Delhi's empires. It's a common reading, but no official statement of that motive has been found.
- **Doesn't hold up:** neat zoning by period. Mughal, Sultanate and viceregal names are mixed together, and some sit far from their namesake's monuments (Tughlak Road is about 11 km from Tughlaqabad as the crow flies). No road was named after Jahangir or the Khaljis.
- **Caveat:** street names come from OpenStreetMap. Old-to-new pairings for viceregal roads follow published lists and are less certain than the rulers' names.


## Double domes

**Claims on the interactive page and the comparison images:**
- **Sikandar Lodi's tomb (1517–18):** often cited as India's first double dome. Some sources call it only a first step, and an earlier tomb in Srinagar (c.1465) has also been proposed. The 1517–18 date and Ibrahim Lodi as builder come from Wikipedia and GKToday; Archnet dates the tomb to Sikandar's reign (1489–1517) and confirms the double dome. ([GKToday](https://www.gktoday.in/double-dome/), [Archnet](https://www.archnet.org/sites/1585))
- **Humayun's Tomb (c.1565–72):** generally credited with the first fully developed Persian-style double dome in India. Its architect, Mirak Mirza Ghiyas, had worked in Herat and Bukhara. ([University of Washington Silk Road project](https://depts.washington.edu/silkroad/cities/india/delhi/humayun/humayun.html))
- **Rashtrapati Bhavan (1912–29):** the official site describes "a lower dome beneath this main dome". The main dome is copper-clad and about 55 m above the forecourt; its outer form is said to draw on the Sanchi stupa. The official Durbar Hall page adds that the inner dome is about 22 m across and 25 m above the ground, with an oculus at its centre; the cutaway shows the oculus. ([President of India](https://www.presidentofindia.gov.in/hi/node/1129), [Rashtrapati Bhavan](https://rashtrapatibhavan.gov.in/rbtour/central-dome), [Durbar Hall](https://rashtrapatibhavan.gov.in/rbtour/durbar-hall))
- **Florence (1420–36):** earlier than Humayun's Tomb but a separate tradition. The double shell and the stone-and-timber chains were already specified in Neri di Fioravanti's 1367 design. Brunelleschi's breakthrough was building it without timber centring, using herringbone brickwork, a pointed ("quinto acuto") profile and new hoists. The thick inner shell carries the load. The theory that Persian domes such as Soltaniyeh influenced Florence (Sanpaolesi, 1972) is real but contested. ([Museo Galileo](https://brunelleschi.imss.fi.it/itineraries/place/TheDomeOfSantaMariaFiore.html) for the dates, the lack of centring and the pointed profile; [Florence Cathedral](https://en.wikipedia.org/wiki/Florence_Cathedral) and its sources for the 1367 model, the chains, herringbone brickwork and hoists; [Dome of Soltaniyeh](https://en.wikipedia.org/wiki/Dome_of_Soltaniyeh))

**Brunelleschi fact-check (Fable, 19 Oct 2026).** Two errors in the first answer were corrected:
- Foundation to finished dome was about **140 years** (1296 to 1436), not 120.
- The double shell wasn't Brunelleschi's invention. Persian double domes were also structural, not just about the skyline.

Nuances: there was no clean winner of the 1418 competition (his scheme was adopted in 1420 with Ghiberti as co-supervisor, and he took sole charge around 1423). The "Gothic and foreign buttresses" motive comes largely from Ross King's narrative. The ball's date is given as 1466, 1469 or 1471. A 1970s survey found no trace of the iron chains.

**Stairs between the shells.**
- **Florence:** visitors climb 463 steps between the shells, and the cutaway shows that climb.
- **Humayun's Tomb:** no stair between the shells is documented. The Aga Khan Trust for Culture, which repaired the cavity in 2009–11, calls the inner dome "barely accessible". Its inner surface "was accessible only through a small opening of 0.8 x 0.6 metre in the neck of the dome", and the team had to put up scaffolding ([AKTC](https://www.nizamuddinrenewal.org/conservation/humayun-tomb/data/dome.php)).
- **Humayun's Tomb, what is documented:** Glenn Lowry's measured roof plan and photograph (Muqarnas 4, 1987) show doorways from the roof terrace into the base of the drum, and what appear to be small stairs in the portal blocks. The cutaway marks the opening and a roof-terrace doorway, and draws no stair.

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

## Domes and roads audit (Fable, 19 Oct 2026, from live web sources)

**Confirmed:**
- Every post-2014 renaming, with its NDMC date.
- That each road's OpenStreetMap name is the right road.
- The namesakes' dates, India Gate (1931) and the dome claims.
- All four photo credits and licences.

**Fixed:**
- Mother Teresa Crescent renaming dated to 2003.
- Spear attribution reworded.
- 1955 renamings described as Nehru's proposal.
- Prithviraj's reign corrected to c.1177–92.
- The Lodi legend's date span.
- Race Club dates.
- The Durbar Hall oculus added to the cutaway.
- Humayun's Tomb dates made consistent.
- Three street labels moved closer to their roads.

## Street-names fact-check (Fable, 19 Oct 2026)

**Confirmed:** every post-2014 renaming and its date, the 1955 Cabinet decision for Rajpath and Janpath, all the old-to-new pairs, the namesakes' dates, India Gate (foundation 1921, inaugurated 12 Feb 1931), and the double-dome claims. The Rashtrapati Bhavan Durbar Hall page itself mentions a "double dome".

**Fixed:**
- Aurangzeb Lane (2023) added.
- Willingdon Crescent dated to the 1930s.
- Race Course Road caveat added.
- Spellings corrected (Tyagraj Marg, Tughlak Road, Feroz Shah Road).
- Namesakes hedged where unsourced.

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
