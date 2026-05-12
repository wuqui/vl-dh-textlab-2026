# Aufgaben

## Inbox

- [ ] TextLab-PM prüfen und dort Reddit-Korpusverfügbarkeit für Deutsch/Englisch planen.
- [ ] vorhandene Workshop-Folien nach wiederverwendbaren Slides, Screenshots und Formulierungen durchsuchen.
- [ ] TextLab-Dokumentation zu Architektur, Korpus-Onboarding, Word Sketches, Semantic Analysis und LLM Classification in Vorlesungssprache übersetzen.
- [ ] Quarto-Render regelmäßig prüfen.
- [ ] Montag-Kurzsmoke vor der Sitzung: Login, DTA Query, Frequency, Reddit-Korpusauswahl, ggf. Word Sketch als Bonuspfad.
- [ ] Vorlesungsaccount am Montag vor der Sitzung nochmal mit Login im UI prüfen.
- [ ] COHA-Integration am Montag kurz gegenprüfen: Korpusauswahl, `[lemma="computer"]`, Frequency nach `decade`.

## Folien-Backlog zur Priorisierung (erfasst 2026-05-11)

### Inhaltlich vorlesungsnah

- [x] Suchen-Slide als Tabelle umbauen: Query | was gefunden wird | Beispiel.
- [x] Query-Setup-Slide so umbauen, dass der Query Builder sichtbar ist und erklärt wird: Man muss dadurch nicht direkt BCQL schreiben.
- [x] Prüfen, ob Semantic-Search-Beispiel und Screenshot im aktuellen Deck gut sichtbar sind; ggf. verbessern.
- [x] Concordance-Beispiel durch COHA-Beispiel ersetzen und NER-Highlights erklären.
- [x] Frequency-Beispiel durch diachrones COHA-Beispiel ersetzen und Buckets chronologisch sortieren.
- [x] Live-Beispielpalette verbessern: German Reddit mit dialektalem DE/AT-Wort; English Reddit mit US/UK-Unterschied.
- [x] Collocation-Beispiel einschlägiger machen, ggf. COHA.
- [x] Topic Modeling vor Embeddings verschieben; Beispiel ergänzen.
- [x] Topic-Modeling-Screenshot ergänzen.
- [ ] Optional ersetzen: spezifischer COHA-topics-over-time-Screenshot, falls später verfügbar.
- [x] Referenzen als Fußnoten/Captions auf relevante Slides verteilen.
- [x] Drei Korpuslogiken: konkrete Beispiele ergänzen.

### Korrektheit und technische Erklärung

- [x] Registry-Codeblock-Kontrast verbessern.
- [x] TEI/XML-Beispiel um Metadaten wie `year` ergänzen.
- [x] Tabelle Daten im TextLab: Größenspalte schmaler.
- [x] Korpuskompilierung: Leading zeros entfernen.
- [x] Suchindex-Folie korrekt erklären: prüfen, welches Format BlackLab tatsächlich nutzt; ggf. als vereinfachtes Vertikalformat labeln.
- [x] BlackLab kurz erklären und offizielle URL verlinken.

### Layout, Plugins und Assets

- [x] Einstieg: Card-Titel `These` zu `TextLab` ändern.
- [x] Word-Sketch-Tabelle: `candidate` als zweite Spalte vor `relation`.
- [x] Quarto Reveal Pointer Plugin installieren/einrichten.
- [x] App-Architekturdiagramm als präzise Quarto/CSS-Grafik passend ins Deck einbauen; ImageGen wegen exakter technischer Labels bewusst nicht verwendet.
- [x] Speaker Notes aus den published slides entfernen bzw. beim Publishing ausschließen.

## TextLab-PM-Backlog (im TextLab-Repo erfasst, keine Umsetzung hier)

- [x] Corpus-Selector zeigt falschen Eintrag `Corpus`; später entfernen/fixen.
- [x] Collocation-Modul liefert bei COHA `[word="computer"]` unplausible Ergebnisse; Stopwords, Ranking, Scoring, Fenster und Attribut prüfen.
- [x] Collocation-Defaults: 3 links / 3 rechts.
- [x] Collocation-Attribut konfigurierbar machen, sinnvoller Default `lemma`.
- [x] Collocation-Metriken konfigurierbar machen; logDice ggf. als Default dokumentieren und mit Literatur/Resource erklären.
- [x] AI Analysis Agent ist nicht zuverlässig genug: Timeouts/Deadline, RAG-Index-Missing, Fehlermeldungen, Chat-Workflow und robuste Tool-Nutzung neu aufsetzen.
- [ ] Query Builder überschreibt die BCQL-Querybox nicht zuverlässig: Wenn dort bereits Text steht, muss man ihn oft erst manuell löschen. Gewünschtes Verhalten klären und sauber fixen, sodass Builder-Ausgabe und BCQL-Preview/Querybox synchron bleiben.
- [ ] Frequency-Modul: Sortierung `Bucket label`/`Ascending` prüfen. Im deployed UI wirkt die Einstellung nicht zuverlässig auf Tabelle/Chart; für diachrone Beispiele müssen Buckets nachvollziehbar chronologisch darstellbar sein.

## In Arbeit

- [ ] Timing nach Probedurchlauf prüfen.

## Erledigt

- [x] Zielscope geklärt: schlankes Repo ohne Worksheets, Query-Dateien, `data/` und `exports/`.
- [x] Scaffold für Repo, Quarto und lokales PM angelegt.
- [x] ersten `quarto render` erfolgreich ausgeführt.
- [x] Folienstruktur in `slides/textlab-ringvorlesung.qmd` in realistische 90-Minuten-Dramaturgie gebracht.
- [x] konkrete Demo-Pfade direkt in den Slides notiert: DTA, `deRed_mini`, `enRed_mid`.
- [x] zentrale TextLab-Screenshots aus dem IDK-Workshop als vorläufige Fallback-Visuals übernommen.
- [x] Architektur-/Methodenfolien um explizite Demo-Regie, Reddit-Kontrast und Mini-Aussage-Vorlage ergänzt.
- [x] Collocation- und Annotation-Fallback-Screenshots aus dem Workshopdeck übernommen.
- [x] `quarto render` nach Folienerweiterung erfolgreich ausgeführt.
- [x] Browser-Check mit Chrome DevTools durchgeführt: keine Console-Fehler, Screenshot-Assets laden, kritische Folien visuell geprüft.
- [x] Vorlesungsaccount auf `dh@lmu.de` umgestellt, freigegeben und per `/auth/me` validiert; alter Lecture-User `textlab-vl-dh-2026@localhost` deaktiviert.
- [x] Montag-MVP für die Vorlesung festgelegt: DTA-Pfad als Pflichtdemo, Reddit als kontrollierter Kontrast, Collocations/Word Sketch/Semantic/LLM als Bonus oder Screenshot.
- [x] Folien auf robuste Demo-Erzählung verdichtet und interne Card-Headings so umgebaut, dass Reveal-Navigation nicht auf den Titel zurückspringt.
- [x] `quarto render` und Playwright-Navigation durch das gesamte Deck geprüft; nur nicht-blockierende Quarto/Reveal-Metawarnung.
- [x] Live-UI-Smoke mit Vorlesungsaccount durchgeführt: Login, Tokenlabels im Korpusmenü, DTA-KWIC/Frequency, German Reddit und English Reddit geprüft.
- [x] Korpuslinguistik-Grundlagenblock mit einschlägigen Literaturverweisen ins Deck eingebaut.
- [x] COHA als live verfügbares diachrones Bonuskorpus in TextLab und Folien eingebaut.
- [x] PDF-Export-Artefakt durch deaktivierte CSS-Shadows behoben und als Runbook-Regel dokumentiert.
