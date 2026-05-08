# Zusammenarbeit: Ringvorlesung Digital Humanities 2026

## Projektkontext

- Anlass: 90-minütige Vorlesung in der Ringvorlesung des Studiengangs Digital Humanities an der LMU.
- Termin: Montag nach dem ITG/IDK-Workshop vom 08.05.2026.
- Thema: Vorstellung von TextLab als DH-/Korpuslabor: Was kann es, wie ist es gebaut, und wie lassen sich zentrale Module methodisch einordnen?
- Primäres Material: Quarto/RevealJS-Folien in `slides/`.
- Ausgangspunkte:
  - TextLab-App und technische Dokumentation: `/Users/quirin/proj/mcl-textlab`
  - heutiger Workshop: `/Users/quirin/itg/idk-workshops/2_text-analysis`
  - ältere MCL-/NoSkE-Korpusbestände: `/Users/quirin/proj/mcl`

## Arbeitsweise

- Dieses Repo ist ein Lehr- und Vorbereitungsrepo, kein TextLab-App-Repo.
- TextLab-Produktarbeit, Korpusimporte, Deployments und technische Backlogs werden im TextLab-Repo geplant und durchgeführt.
- Lokales Projektmanagement für diese Vorlesung liegt in `.agents/`.
- Externe deutschsprachige Texte verwenden reguläre Umlaute und `ß`.
- Literaturangaben werden bei Bedarf über Quarto-native Citations in `references.bib` gepflegt.
- Keine großen Korpora, BlackLab-Indizes oder Runtime-Daten in dieses Repo kopieren.

## Dateien in `.agents/`

- `context.md`: Rahmenbedingungen, Zielgruppe, Quellen und Annahmen.
- `project.md`: Entscheidungen, Arbeitsplan, offene Fragen und Risiken.
- `tasks.md`: konkrete Aufgabenliste mit Status.
- `lecture-outline.md`: inhaltlicher Ablauf und Folienstruktur.
- `runbook.md`: Arbeits- und Renderhinweise für die Vorbereitung.

## Leitplanken

- Die Vorlesung soll TextLab zugleich als nutzbares Werkzeug und als gebaute Infrastruktur erklären.
- Jede Modulvorstellung soll drei Ebenen verbinden: Use Case, sichtbare Oberfläche, technische Grundlage.
- Hands-on-Anteile können direkt in die Folien integriert werden; separate Übungsblätter werden nur bei Bedarf angelegt.
- Reddit-Korpora dienen als anschauliche, gegenwartsnahe Demo-Korpora; die operative Planung ihrer Verfügbarkeit passiert im TextLab-PM.
