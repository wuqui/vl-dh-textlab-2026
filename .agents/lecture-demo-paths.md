# TextLab-Vorlesung: getestete Demo-Pfade

Stand: 2026-05-10, live gegen `https://www.wuerschinger.org/textlab/` geprüft.

Keine Credentials in Slides oder Public-Repo aufnehmen.

## Robuste Hauptpfade

### DTA: Einstieg, KWIC, Frequency

- Korpus: `dta_full_uncapped`
- Query: `[lemma="Demokratie"]`
- Ergebnis: 2,486 Treffer, Query ca. 74 ms
- Frequency: `group_by=metadata`, `attribute=year`
- Gute sichtbare Werte:
  - 1848: 1,252 Treffer, ca. 187.9 pro Mio. Tokens
  - 1893: 174 Treffer, ca. 236.1 pro Mio. Tokens
  - 1875: 125 Treffer, ca. 149.8 pro Mio. Tokens
- Demo-Punkt: KWIC -> Frequenz nach Jahr -> zurück in Belege.

### COHA: diachroner Bedeutungs-/Gebrauchswandel

- Korpus: `coha`
- Query: `[lemma="computer"]`
- Ergebnis: 14,830 Treffer, Query ca. 97 ms
- Frequency: `group_by=metadata`, `attribute=decade`
- Gute sichtbare Werte:
  - 1870: 3 Treffer, historisch noch als menschlicher Rechner plausibel.
  - 1950: 131 Treffer.
  - 1980: 3,773 Treffer.
  - 1990: 4,946 Treffer.
  - 2000: 3,830 Treffer.
- Demo-Punkt: dieselbe Lemma-Query zeigt in KWIC alte Bedeutungen und in Frequency die technische Massenverbreitung.

### English Reddit: Community-Kontrast

- Korpus: `enRed_mid`
- Query: `[word="Wales"]`
- Frequency: `group_by=metadata`, `attribute=subreddit`
- Ergebnis: 46,003 Treffer, Distribution ca. 901 ms
- Gute sichtbare Werte:
  - Wales: 43,258 Treffer, ca. 5,487.8 pro Mio. Tokens
  - Scotland: 1,478 Treffer
  - AskUK: 665 Treffer
  - northernireland: 496 Treffer
  - AskAnAmerican: 106 Treffer
- Demo-Punkt: Korpusmetadaten sind nicht Deko, sondern machen Variation sichtbar.

### German Reddit: Community-/Register-Kontrast

- Korpus: `deRed_mini`
- Query: `[lemma="deutsch"]`
- Frequency: `group_by=metadata`, `attribute=subreddit`
- Ergebnis: 33,122 Treffer, Distribution ca. 1.8 s
- Gute sichtbare Werte:
  - de: 10,990 Treffer
  - ich_iel: 5,976 Treffer, auffällig hohe normalisierte Rate
  - FragReddit: 5,410 Treffer
  - Austria: 2,941 Treffer
  - Finanzen: 1,982 Treffer
- Demo-Punkt: absolute Counts und normalisierte Raten erzählen nicht immer dieselbe Geschichte.

## Explorative Module

### Collocations

- Korpus: `dta_full_uncapped`
- Query: `[lemma="Demokratie"]`
- Parameter: `context_tokens=5`, `max_hits=500`, `min_count=5`, `attribute=lemma`, `direction=both`, `include_stopwords=false`
- Laufzeit: ca. 1.9 s
- Gute Kandidaten:
  - `organ`, `zeitung`, `köln`, `neu`, `rheinische`
- Demo-Punkt: Ergebnis zeigt auch Corpus-/Dokumenteffekte, hier stark: Neue Rheinische Zeitung / Organ der Demokratie.

### Word Sketch

- Korpus: `dta_full_uncapped`
- Lemma: `Demokratie`
- Parameter: `max_hits=500`, `min_count=2`, `max_items_per_relation=5`
- Laufzeit: ca. 8.9 s
- Gute Kandidaten:
  - Modifiers: `sozial`, `reprasentativ`, `europaisch`
  - Governing verbs: `siegte`, `lasse`, `trat`
  - Nominal associations: `organ`, `rechtsgeschichte`, `gunsten`, `prinzipien`, `sieg`
- Demo-Punkt: POC ist erklärbar, aber nicht als vollständiges Sketch-Engine-Äquivalent framen.

### Semantic Search

- Korpus: `dta_full_uncapped`
- Query: `politische Freiheit und Demokratie`
- Parameter: `top_k=5`, `candidate_pool=80`, `lexical_probe_hits=80`
- Laufzeit: ca. 4.3 s
- Gute Ergebnisse:
  - Bayerische Presse 1850 zu demokratischem Princip.
  - Social-politische Blätter 1874 zu Vereins-/Versammlungsrecht und politischer Freiheit.
  - Mainzer Journal 1848 zu Freiheit.
- Demo-Punkt: anderer Suchmodus als BCQL, aber Rückbindung an Belege bleibt entscheidend.

## Zeitlogik für Live-Demo

- Sicherster Pfad: DTA Query -> KWIC -> Frequency year.
- Wenn Zeit: COHA `[lemma="computer"]` -> Frequency decade -> KWIC mit alten Bedeutungen.
- Wenn Publikum aktiv ist: Reddit `Wales` oder `deutsch` -> Frequency subreddit.
- Explorative Module nur zeigen, wenn die Verbindung stabil wirkt:
  - Collocations ist schnell genug.
  - Word Sketch ist etwas langsamer, aber noch vorführbar.
  - Semantic Search ist als Methodenblick gut, aber nicht als harte Live-Abhängigkeit nötig.
