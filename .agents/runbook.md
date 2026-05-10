# Runbook

## Render

```bash
quarto render
```

## Quarto/RevealJS-Fallen

- In `revealjs`-Folien keine Markdown-Überschriften (`#`, `##`, `###`, ...) innerhalb von Cards, Columns, Callouts, HTML-Blöcken oder anderen Container-Layouts verwenden.
- Reveal interpretiert Markdown-Headings als Slide-/Section-Struktur. Besonders `###` innerhalb einer Folie kann als nested vertical section gerendert werden und die Navigation nach einigen Slides abbrechen oder auf `#1` zurückspringen lassen.
- Für Card-interne Titel stattdessen HTML verwenden, z. B. `<h3>Live</h3>`, oder reine Markdown-Fettschrift wie `**Live**`, wenn kein semantisches Heading nötig ist.
- Nach strukturellen Folienänderungen immer `quarto render` ausführen und im gerenderten HTML prüfen, ob keine unerwarteten nested Reveal-Sections entstanden sind. Ein schneller Check ist:

```bash
rg '<section[^>]*>\\s*<section' _site/slides/textlab-ringvorlesung.html
```

- Wenn die Navigation im Browser nach einer bestimmten Folie springt, zuerst die vorherige Folie auf interne Markdown-Headings in Cards/Columns prüfen.

## Live-Smoke 2026-05-09

TextLab live:

- URL: `https://www.wuerschinger.org/textlab/`
- App shell: 200
- Auth route: `/auth/login` routed to `textlab-api.service`
- Services: `textlab-api.service`, `nginx.service`, `blacklab.service` active
- Probe account: server-side in `/etc/textlab/textlab_probe_auth.env`
- Vorlesungsaccount: `dh@lmu.de`, approved non-admin user, credentials server-side in `/etc/textlab/textlab_lecture_auth.env`

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
2. Folien in `slides/textlab-ringvorlesung.qmd` bearbeiten.
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
