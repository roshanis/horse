# Travancore, 1671 to 1758: a reading atlas

An interactive atlas of Mark de Lannoy, *The Kulasekhara Perumals of Travancore: History and State Formation in Travancore from 1671 to 1758* (Leiden: Research School CNWS, 1997), made as research for the novel *Horse of the Servant*.

Open `index.html` in a browser. It is a single self-contained page.

## What is in it

- **Atlas and timeline.** All 260 dated events in the book, from 1671 to the epilogue in 1809. Each has its printed page, the quote where there is one, and the archive record de Lannoy cites. Scroll the timeline and the map follows, or drag the year slider.
- **The map.** Real terrain, coastline, backwaters and rivers. It shows who held each of 14 principalities in any year, with campaign routes, defence lines, and Dutch, English and French posts.
- **How the kingdom grew.** One bar per principality, 1700 to 1760.
- **Colachel.** A close-up of the 1741 siege on the real coast of the far south.
- **Houses and people.** The three royal branches, the Venad line by adoption, and 36 people.
- **Key terms**, from the book's glossary.
- **Against the Historical Note.** Twenty points where the book differs from, or adds to, the novel's Historical Note.
- **Slips and places.** Seven places where the book contradicts itself, and a gazetteer of all 78 places with how each was identified.

## Files

| Path | Contents |
| --- | --- |
| `index.html` | The built page |
| `data/events.jsonl` | One event per line: `y m d approx` date, `t` title, `x` summary, `p` printed page, `pl` places, `pp` people, `k` kind, `q`/`qp` quote and page, `src` record cited, `note` where the book contradicts itself |
| `data/places.json` | Coordinates, modern name, certainty (1 sure, 2 approximate, 3 guess), number on the book's own map |
| `data/regions.json` | Approximate principality outlines in map pixel space |
| `data/water.json`, `data/contours.json`, `data/shade.png` | Sea, backwaters, rivers, elevation bands and hillshade |
| `src/content.py` | Era narratives, territory status by year, routes, lines, posts, people, terms, the Note comparison and the slips |
| `src/template.html`, `src/build.py` | Page template and build script: `python3 src/build.py` rewrites `index.html` |

## Sources and caveats

- Text read from an OCR copy of the book, so a few figures may carry scanning errors. Page numbers are the printed pages.
- Summaries and era narratives are my own; quotations are short and attributed.
- Terrain is from open elevation data. Water is from OpenStreetMap via Overture Maps, with modern dams, canals and straight drainage cuts removed where they could be detected.
- The map uses Web Mercator at zoom 10, tiles x 726 to 735 and y 480 to 489, giving 2560 by 2560 pixels.
- Principality borders are approximate reconstructions from the book's maps and the watershed of the Ghats, not surveyed lines.
- Some places could not be located. Paterre, the king's camp after Colachel, is one; de Lannoy could not find it either.
