# Vorlesungsoutline

## Q

### Top-Level-Plan v2 mit Timing

**10:15-10:22 Einstieg: Korpuslinguistik/Textanalyse und was man damit machen kann**

- Ziel: Lust auf die Breite der Operationen machen, nicht defensiv mit Grenzen starten.
- Leitfrage: Wie werden große Textsammlungen zu untersuchbaren Daten?
- TextLab als durchgehendes Beispiel: Daten, Suche, Analyse, KI-Module.
- Preview: Belege öffnen, Muster vergleichen, Kollokationen/Sketches, Semantic Search, Topic Modeling, LLM Classification, AI Analysis.

**10:22-10:32 Architektur der App: Wie ist TextLab grundsätzlich gebaut?**

- Ziel: Vor den Fachkonzepten einmal die Gesamtmaschine sichtbar machen.
- Schichten: Korpora/Rohdaten -> Korpuskompilierung/NLP -> BlackLab/Index -> TextLab API -> UI/Analyse-Module.
- Wichtige Idee: Die Oberfläche ist nicht nur Suchbox, sondern Workflow über verschiedene Backend-Fähigkeiten.
- Registry als Brücke: Korpus-Metadaten, verfügbare Felder, Labels, Capabilities, kuratierte Value-Options.
- Kurz zeigen: Warum Architektur bestimmt, welche Methoden praktisch möglich sind.

**10:32-10:42 Hintergrund Korpuslinguistik: wichtige Konzepte**

- Korpus, Dokument, Token, Lemma, Annotation, Metadaten.
- Query, Trefferraum, KWIC/Konkordanz, Frequenz, Normalisierung.
- Punkt: Konzepte nur so weit erklären, wie sie gleich im Tool gebraucht werden.

**10:42-10:52 Data: Korpora im TextLab**

- DTA: historisches Deutsch, diachrone Belege, DTA als stabiler Einstieg.
- Reddit: Gegenwartssprache, Community-/Subreddit-Kontraste, Plattformdaten.
- COHA: historisches Englisch, Genres, 19./20./21. Jahrhundert, Lexical Change.
- Ziel: Unterschiedliche Korpuslogiken führen zu unterschiedlichen Fragen.

**10:52-11:02 Korpuskompilierung: Wie Daten suchbar werden**

- Sampling/Selektion, Dokumentmodell, Metadaten.
- NLP: Tokenisierung, Lemmatisierung, POS, Dependencies, NER.
- Indexing: BlackLab/BCQL, Dokumentfelder, Tokenattribute.
- Beispiele: Warum COHA-Chunks, Reddit-Metadaten und DTA-Jahre für die späteren Module wichtig sind.

**11:02-11:12 Suchen: von Begriff zu Trefferraum**

- CQL/BCQL-Suche: `word`, `lemma`, Regex, einfache Filter.
- Query Builder als UI-Schicht über strukturierten Suchoperationen.
- Semantische Suche als anderer Suchmodus: von exakter Form zu Ähnlichkeit im Embedding-Raum.
- Live-Pfad: DTA `Demokratie` oder `Freiheit`.

**11:12-11:25 Ergebnisse analysieren I: Konkordanzen und Frequenzen**

- Konkordanzen: Treffer als Belege, schnelle Kontextlektüre, Detailansicht.
- Frequenzanalyse: Treffer gruppieren und vergleichen.
- Regionale/Community-Unterschiede: z. B. DE vs AT oder Subreddit-Kontraste auf deRed.
- Diachroner Wandel: z. B. `telephone` vs `phone` vs `smartphone` in COHA.

**11:25-11:32 Hands-on 1**

- Aufgabe: Eine Query ausführen, KWIC prüfen, eine Frequenzgruppierung ansehen.
- Minimalpfad: DTA `Demokratie` oder `Freiheit`.
- Optional: COHA `computer`/`telephone` oder Reddit `deutsch`.

**11:32-11:40 Ergebnisse analysieren II: explorative und KI-gestützte Module**

- Kollokationen und Word Sketches: typische Umgebungen und grammatische Profile.
- Beispielidee: Wandel von `gay` auf COHA oder ein stabileres Demo-Lemma, falls live besser.
- Topic Modeling: Korpus-/Dokumentthemen als stabilere Attribute vs on-the-fly Query-Topic-Modeling.
- LLM Classification: Treffer oder Dokumente nach Schema labeln.
- AI Analysis: Agentisches Zusammenführen von Suchschritten, Evidenz und Rückfragen.

**11:40-11:45 Abschluss: Von Demo zu eigener Fragestellung**

- Takeaway: Daten wählen, Query starten, Modul wechseln, nächste Frage formulieren.
- Reproduzierbarkeit: Query, Korpus, Filter, Modul, Parameter und Beispiele festhalten.
- Kurzer Hinweis auf Literatur/Links; keine internen Checklisten im sichtbaren Deck.

## Arbeitstitel

TextLab in den Digital Humanities: Korpora, Suche, Muster und KI-gestützte Exploration

## Leitidee

TextLab wird als Beispiel dafür erklärt, wie DH-Infrastruktur entsteht: Daten werden kuratiert, annotiert, indexiert, über eine Oberfläche bedienbar gemacht und durch Analyse-/KI-Module erweitert.

## Block 1: Korpuslabor und Belegarbeit

Ziel: Die Studierenden verstehen, warum Korpusarbeit nicht mit einer Suchbox beginnt, sondern mit Datenmodellierung, Annotation und Indexierung.

Mögliche Folien:

- Was ist TextLab?
- Architektur in 5 Schichten: Daten, Annotation, Index, API, UI.
- Korpus-Ingestion: Rohdaten zu suchbaren Korpora.
- DTA und Reddit als unterschiedliche Korpuslogiken.
- Concordance/KWIC: Treffer als Belege.
- Frequency: Treffer als Verteilungen.
- Hands-on: Query, KWIC, Frequenz, vorsichtige Aussage.

## Block 2: Explorative und KI-gestützte Module

Ziel: Die Studierenden sehen, wie TextLab über Suche und Zählen hinausgeht, ohne die Rückbindung an Belege aufzugeben.

Mögliche Folien:

- Kollokationen: typische Umgebungen.
- Word Sketches: Relation, Kandidat, Frequenz, Score.
- Semantic Analysis: Embeddings, Cluster, Bedeutungsräume.
- Semantic Search: Anfrage als semantischer Suchraum.
- LLM Classification: kontrollierte Stichprobenannotation.
- Grenzen: Modellannahmen, Reproduzierbarkeit, Bias, Kosten, Datenschutz.
- Hands-on: exploratives Modul testen und interpretieren.

## Schluss

TextLab ist nicht nur ein Tool, sondern ein Argument darüber, wie DH-Methoden praktisch operationalisiert werden: transparent genug für Lehre, flexibel genug für Forschung, aber immer abhängig von Korpusentscheidungen und Modellannahmen.
