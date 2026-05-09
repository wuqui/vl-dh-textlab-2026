# Runbook

## Render

```bash
quarto render
```

## Live-Smoke 2026-05-09

TextLab live:

- URL: `https://www.wuerschinger.org/textlab/`
- App shell: 200
- Auth route: `/auth/login` routed to `textlab-api.service`
- Services: `textlab-api.service`, `nginx.service`, `blacklab.service` active
- Probe account: server-side in `/etc/textlab/textlab_probe_auth.env`
- Vorlesungsaccount: `textlab-vl-dh-2026@localhost`, approved non-admin user, credentials server-side in `/etc/textlab/textlab_lecture_auth.env`

Confirmed demo queries through authenticated TextLab API:

| Korpus | Query | Treffer | Distribution |
|---|---:|---:|---|
| `dta_full_uncapped` | `[lemma="Demokratie"]` | 2,486 | `year`: top `1848` = 1,252 |
| `deRed_mini` | `[lemma="deutsch"]` | 33,122 | `subreddit`: top `de` = 10,990, `ich_iel` = 5,976 |
| `enRed_mid` | `[word="Wales"]` | 46,003 | `subreddit`: top `Wales` = 43,258 |

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
