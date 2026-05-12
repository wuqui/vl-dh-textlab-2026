# Runbook

## Render

```bash
quarto render
```

## PDF-Export

```bash
quarto render
npx decktape reveal _site/index.html output/textlab-ringvorlesung.pdf
```

Nach dem Export mindestens eine Card-/Table-Folie als PNG prüfen:

```bash
pdftoppm -png -f 2 -l 2 -r 150 output/textlab-ringvorlesung.pdf output/pdf-check/page
```

Wichtig: CSS-`box-shadow` ist für decktape/PDF in diesem Deck deaktiviert. Weiche Schatten können im PDF als große graue Rechteckflächen erscheinen, besonders in macOS Preview/Acrobat. Für neue Card-, Tabellen-, Bild- oder Codeblock-Styles deshalb keine `box-shadow`-Regeln wieder einführen, ohne den PDF-Export visuell zu prüfen.

## Quarto/RevealJS-Fallen

- In `revealjs`-Folien keine Markdown-Überschriften (`#`, `##`, `###`, ...) innerhalb von Cards, Columns, Callouts, HTML-Blöcken oder anderen Container-Layouts verwenden.
- Reveal interpretiert Markdown-Headings als Slide-/Section-Struktur. Besonders `###` innerhalb einer Folie kann als nested vertical section gerendert werden und die Navigation nach einigen Slides abbrechen oder auf `#1` zurückspringen lassen.
- Für Card-interne Titel stattdessen HTML verwenden, z. B. `<h3>Live</h3>`, oder reine Markdown-Fettschrift wie `**Live**`, wenn kein semantisches Heading nötig ist.
- Nach strukturellen Folienänderungen immer `quarto render` ausführen und im gerenderten HTML prüfen, ob keine unerwarteten nested Reveal-Sections entstanden sind. Ein schneller Check ist:

```bash
rg '<section[^>]*>\\s*<section' _site/index.html
```

- Wenn die Navigation im Browser nach einer bestimmten Folie springt, zuerst die vorherige Folie auf interne Markdown-Headings in Cards/Columns prüfen.

## Reveal Pointer

- Die Quarto-Extension `quarto-ext/pointer` ist lokal unter `_extensions/quarto-ext/pointer/` installiert.
- In der Präsentation toggelt `q` den Pointer; Farbe und Größe sind im YAML von `index.qmd` gesetzt.
- Nach Quarto-Upgrades einmal prüfen, ob `site_libs/revealjs/plugin/reveal-pointer/pointer.js` im gerenderten HTML geladen wird.

## Browser-Workflow für Reviews und Screenshots

0. Für Screenshot-Arbeit zuerst den persönlichen Codex-Skill `$browser-screenshot-workflow` verwenden; die projektspezifischen Regeln hier ergänzen diesen Workflow.
1. Sichtbarer Codex-Browser / In-app-Browser ist der Default für Folienreviews, `file://`, `localhost` und öffentliche Seiten ohne Login.
2. Für `https://www.wuerschinger.org/textlab/` mit Login die Codex Chrome Extension verwenden. Sie ist der richtige Weg, wenn Codex den eingeloggten Nutzerzustand aus Chrome sehen soll.
3. Nicht zwischen In-app-Browser, Chrome DevTools und Playwright wechseln, ohne den Kontext explizit zu benennen. Wenn ein Tool Login-Screen zeigt, während der Nutzer eine eingeloggte Seite sieht, ist es der falsche Browser-Kontext.
4. Chrome DevTools nur gezielt einsetzen: DOM-Inspektion, Network-Fehler, Console-Fehler, CSS-Diagnose. Vor Aktionen prüfen, dass URL und Session sichtbar zum Nutzerzustand passen.
5. Playwright nur für reproduzierbare Abläufe verwenden: DeckTape/PDF-Export, automatisierte Navigation, E2E-Smokes oder Screenshot-Serien, die bewusst aus einem Skript kommen.
6. Screenshot-Assets für das Deck müssen mit ihrer Herkunft benannt werden:
   - `live-deployed-*`: aus der deployed TextLab-App
   - `local-*`: aus lokaler App
   - `deck-*`: aus gerendertem Deck
   - `fallback-*`: historische Doku-/Workshopbilder, nur wenn ausdrücklich als Fallback gewünscht
7. Für Folien-Screenshots zuerst Element-Screenshots versuchen. Wenn ein Fullpage-Screenshot zugeschnitten werden muss, `.agents/crop-screenshot.py` verwenden:
   - `python3 .agents/crop-screenshot.py info <image>`
   - `python3 .agents/crop-screenshot.py contact <image> /tmp/contact.png --strip-height 900`
   - `python3 .agents/crop-screenshot.py candidates <image> /tmp/crops --x 60 --width 2760 --height 900 --ys 1200,1500,1800`
   - `python3 .agents/crop-screenshot.py crop <image> <output> --x 60 --y 1500 --width 2760 --height 900 --spec assets/screenshots/textlab/crops.json`

## Live-Smoke 2026-05-09

TextLab live:

- URL: `https://www.wuerschinger.org/textlab/`
- App shell: 200
- Auth route: `/auth/login` routed to `textlab-api.service`
- Services: `textlab-api.service`, `nginx.service`, `blacklab.service` active
- Probe account: server-side in `/etc/textlab/textlab_probe_auth.env`
- Vorlesungsaccount: `dh@lmu.de`, approved non-admin user, credentials server-side in `/etc/textlab/textlab_lecture_auth.env`
- 2026-05-11: Vorlesungsaccount nach GitGuardian-Alert gelöscht und neu angelegt; Login und `/api/textlab/health` mit neuer serverseitiger Credential-Datei erfolgreich geprüft.
- 2026-05-11: Git-Historie auf `main` bereinigt und force-gepusht; Publish-Workflow währenddessen pausiert und danach wieder aktiviert. Remote-`main` und `gh-pages` auf Zugangsdaten-Zeilen geprüft.

Confirmed demo queries through authenticated TextLab API:

| Korpus | Query | Treffer | Distribution |
|---|---:|---:|---|
| `dta_full_uncapped` | `[lemma="Demokratie"]` | 2,486 | `year`: top `1848` = 1,252 |
| `deRed_mini` | `[lemma="deutsch"]` | 33,122 | `subreddit`: top `de` = 10,990, `ich_iel` = 5,976 |
| `enRed_mid` | `[word="Wales"]` | 46,003 | `subreddit`: top `Wales` = 43,258 |

Confirmed through live UI with the lecture account:

- Login as `dh@lmu.de` succeeds in the browser.
- Corpus selector shows token counts, not document counts:
  - DTA: `238.3M tokens`
  - English Reddit: `41.3M tokens`
  - German Reddit memes: `4.4M tokens`
  - German Reddit: `61.2M tokens`
- DTA UI path works: `[lemma="Demokratie"]`, concordance `Showing hits 1-10 of 2486`, frequency by `year`, top `1848` = `1.252`.
- German Reddit UI path works: `[lemma="deutsch"]`, frequency by `subreddit`, total hits `33.122`, top `de` = `10.990`, `ich_iel` = `5.976`, `FragReddit` = `5.410`.
- English Reddit UI path works: `[word="Wales"]`, concordance `Showing hits 1-10 of 46003`, frequency by `subreddit`, total hits `46.003`, top `Wales` = `43.258`, `Scotland` = `1.478`, `AskUK` = `665`.

Live input hygiene: after running a query, check `Last executed query` before interpreting results. If a tab still shows old controls after switching corpora, rerun the active result tab explicitly.

Live-demo rule: show DTA first; only show Reddit after DTA query + distribution are stable. Use screenshot fallback for Collocations, Word Sketch and Annotation if runtime or room conditions are weak.

## Lokale Arbeitsreihenfolge

1. `.agents/project.md` und `.agents/tasks.md` prüfen.
2. Folien in `index.qmd` bearbeiten.
3. Bei neuen technischen Aussagen TextLab-Doku in `/Users/quirin/proj/mcl-textlab/dev/docs/` prüfen.
4. Bei wiederverwendbaren Workshopteilen Material in `/Users/quirin/itg/idk-workshops/2_text-analysis` prüfen.
5. Rendern und sichtbare Probleme direkt korrigieren.

## Abgrenzung zum TextLab-Repo

In dieses Repo gehören:

- Vorlesungsfolien
- lokale Vorbereitungsnotizen
- ggf. spätere Screenshots oder kleine öffentliche Fallback-Artefakte

Ins TextLab-Repo gehören:

- Korpusimporte
- TextLab-Backlog
- Deployments
- Auth/Account-Themen
- technische Feature-Fixes
- Benchmarks und Smoke-Tests der App
