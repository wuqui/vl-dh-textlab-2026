# Projektmanagement

## Zielbild

Ein fokussiertes Quarto-/RevealJS-Deck für eine 90-minütige Ringvorlesung über TextLab als DH-Infrastruktur und Analyseumgebung.

## Entscheidungen

- Dieses Repo enthält nur Vorlesungsmaterialien und lokales Vorbereitungs-PM.
- Keine separaten Übungsblätter zum Start.
- Keine separaten Query-Set-Dateien zum Start.
- Keine `data/`- oder `exports/`-Ordner zum Start.
- TextLab-Fixes, Korpusimporte und Reddit-Korpusplanung werden im TextLab-Repo und dessen PM bearbeitet.
- Die Folien dürfen zunächst als integriertes Arbeitsdeck wachsen.
- Hands-on-Schritte werden vorerst direkt in den Slides geführt.
- Workshop-Screenshots dienen als Fallback-Visuals; der finale Live-Smoke hat die Montag-MVP-Pfade zusätzlich im laufenden UI bestätigt.
- Für Montag bleibt DTA + Reddit der robuste MVP. COHA ist zusätzlich als frisch importierter Bonuspfad live verfügbar und passt als diachrones englisches Brückenkorpus methodisch sehr gut.
- Nach der VL ist der harte Deploy-Freeze aufgehoben: Deploys sind wieder möglich, wenn sie sinnvoll sind und zum jeweiligen Arbeitspaket passen.

## Vorläufige Vorlesungsstruktur

- Block 1: TextLab als Korpuslabor, Architektur, Korpus-Ingestion, Concordance/KWIC, Frequency.
- Hands-on 1: Query, KWIC, Frequenz, vorsichtige Aussage.
- Block 2: Collocations, Word Sketches, Semantic Analysis, Semantic Search, LLM Classification.
- Optionaler Einschub: COHA als historisches englisches Vergleichskorpus.
- Hands-on 2: exploratives Modul an einem Demo-Korpus.
- Abschluss: Was zeigt TextLab über DH-Infrastruktur, Modellierung und Interpretation?

## Offene Fragen

- Soll der Schwerpunkt stärker auf Reddit-Korpora oder stärker auf DTA/TextLab allgemein liegen?
- Welche TextLab-Module sind live stabil genug für Vorführung statt Screenshot?
- Gibt es Raum-/Netz-/Account-Anforderungen für die Hands-on-Anteile?
- Reichen Workshop-Fallbacks für Montag, oder sollen nachträglich noch frische UI-Screenshots ins Deck?
- Soll COHA im Live-Ablauf kurz gezeigt werden oder nur als optionaler Bonuspfad bereitstehen?
- Priorisierung offen: Welche der am 2026-05-11 erfassten Folien-To-dos müssen noch vor der VL ins Deck, welche reichen als Post-VL-Aufräumarbeiten?

## Risiken

- Zu viele Module können die 90 Minuten überladen.
- Live-Demos hängen an TextLab-Verfügbarkeit, Auth, Netz und Korpusindizes.
- Technische Architektur darf die methodische Anschlussfähigkeit nicht verdrängen.
- Reddit-Korpora sind anschaulich, brauchen aber klare Kontextualisierung: Plattformdaten, Sampling, Moderation, Sprache, Ethik.

## Priorisierungsvorschlag 2026-05-11 (noch nicht bestätigt)

### Noch vor der VL ins Deck

- Suchen-/Query-Setup-Folien vereinfachen: Suchbeispiele als Tabelle, Query Builder sichtbar machen, BCQL als technische Grundlage erklären.
- COHA in Concordance und Frequency stärker nutzen: diachrone Beispiele, chronologisch sortierte Buckets, NER-Highlights dort erklären, wo sie sichtbar sind.
- Modulreihenfolge didaktisch glätten: Topic Modeling vor Embeddings/Semantic Search verschieben und mit gut sichtbarem Beispiel/Screenshot absichern.
- Architektur- und Datenfolien fachlich schärfen: BlackLab kurz erklären und verlinken, Suchindex-Format korrekt bzw. als vereinfachtes Vertikalformat labeln, TEI/XML-Metadaten ergänzen.
- Sichtbarkeit und Lesbarkeit verbessern: Semantic-Search-Screenshot prüfen, Registry-Codeblock-Kontrast erhöhen, Daten-Tabelle schmalere Größenspalte, Einstiegstitel `TextLab`, Word-Sketch-Spaltenreihenfolge.
- Live-Beispielpalette finalisieren: German Reddit DE/AT-dialektal, English Reddit US/UK, Collocation-Beispiel einschlägiger machen.

### TextLab-PM, nicht im Lecture-Repo umsetzen

- Corpus-Selector-Bug, Collocation-Modul/Defaults/Attribute/Metriken und AI-Analysis-Agent-Zuverlässigkeit gehören ins TextLab-Backlog.
- TextLab-Produktarbeit, Korpusimporte und Deployments bleiben im TextLab-Repo; nach der VL sind Deploys wieder möglich, wenn sie zum jeweiligen Arbeitspaket passen.

### Nach der VL ausreichend

- Referenzen systematisch als Fußnoten/Captions auf relevante Slides verteilen, falls die schnelle Vorlesungsfassung sonst stabil ist.
- Quarto Reveal Pointer Plugin installieren/einrichten, sofern kein akuter Präsentationsbedarf besteht.
- App-Architekturdiagramm per Image Gen erstellen und gestalterisch ins Deck integrieren, sofern die aktuelle Architekturfolie für die VL genügt.
- Korpuskompilierung kosmetisch bereinigen, z. B. Leading zeros entfernen, sofern dadurch keine fachliche Fehlinterpretation entsteht.
