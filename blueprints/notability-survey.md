# Notability handwritten-notes survey

Surveyed 2026-08-06 on Boran's Mac. **Nothing was extracted or converted** — this is the locate-and-
identify pass only. All paths are local to that machine; a cloud agent cannot reach any of it.

## Where the notes actually are

```
~/Library/Mobile Documents/ZP9ZJ4EF3S~com~gingerlabs~Notability/Documents/
```

**337 `.nbn` bundles.** Two other Notability locations look plausible but are **empty** — don't waste
time there:

- `~/Library/Mobile Documents/iCloud~com~gingerlabs~Notability/Documents/` — empty
- `~/Library/Containers/com.gingerlabs.Notability/Data/Documents/` — empty

One gotcha: `ls`/`stat` over the iCloud path stalls badly (iCloud materialises files on stat). `find`
without `-exec stat` is fast; anything that stats all 337 bundles takes several minutes.

## What an `.nbn` actually is

It is a **directory bundle**, not a flat file:

| Entry | Contents |
|---|---|
| `Session.plist` | The handwriting itself — proprietary binary stroke data. **This is the ink.** |
| `PDFs/*.pdf` | The original imported document used as the page background (absent for notes drawn from scratch) |
| `Images/*.png` | Pasted images |
| `thumb12x.png` | First-page thumbnail |
| `metadata.plist` | Title, dates |
| `HandwritingIndex/index.plist` | Notability's own handwriting-recognition index |

The consequence that governs everything below: **`Session.plist` holds the handwriting in an
undocumented format, and `PDFs/` holds the background *without* the handwriting.** Pulling the PDF out
of a bundle gives you the professor's clean slides or the textbook page — not Boran's work.

## Composition of the library

| Category | Count |
|---|---|
| Total bundles | 337 |
| Pure handwriting (no imported PDF) | 61 |
| Annotated on top of an imported PDF | 276 |
| Substantial ink (Session.plist > 200 KB) | 170 |
| Trivial ink (< 20 KB — imported, barely marked) | 91 |

Ink size is the useful proxy for "how much of this is actually Boran's own writing."

## Conversion: the honest answer

**There is no reliable third-party `.nbn` → PDF converter, and extraction won't reproduce the notes.**
The ink lives in an undocumented binary plist; no maintained open-source tool renders it. Any script
that "converts" an `.nbn` really just copies the embedded background PDF out, losing the handwriting —
which is the entire value here.

The only faithful path is **Notability's own export**, which flattens ink onto the background:

1. **Batch, whole library — recommended.** Notability → Settings → **Auto-backup**, set format to **PDF**
   and pick a destination (Google Drive / Dropbox / Box / OneDrive). It exports the entire library,
   preserving the subject/divider structure, and keeps it current.
2. **Selective.** In the note list, multi-select → **Share / Export → PDF**. Right for pulling a
   specific course.
3. Boran's iPad is likely the better device to drive this from — the Mac library shows no subject
   organisation, and the notes were almost certainly written on the iPad.

Export quality caveat: PDF export rasterises/flattens, so an annotated textbook exports *with* the
textbook page underneath. That matters for what can be published — see below.

## Publication triage

### Safe — Boran's own work

The **61 pure-handwriting bundles** are the clean set: no imported source, all his. The largest:

| Ink | Name |
|---|---|
| 22.6 MB | Note 24 Sep 2024 (2) (2) |
| 19.6 MB | Note 30 Sep 2025 |
| 16.0 MB | Note 23 Jan 2026 |
| 15.1 MB | Note 10 Feb 2025 |
| 13.2 MB | Note 23 Sep 2024 |
| 10.5 MB | Note 19 Feb 2025 |
| 10.4 MB | Note 11 Feb 2025 |
| 8.3 MB | Note 20 Jan 2026 |

They're named only by date, so **their subject is unknown without opening them.** That's the main
remaining unknown in this survey. `thumb12x.png` in each bundle is a first-page thumbnail and is the
cheapest way to identify them in bulk.

Also safe: `art_history_study_notes_for_MT1_boran_kilic` — self-labelled as his own study notes.

### Do not publish — copyrighted source underneath

The 276 PDF-backed bundles are annotations *on someone else's document*. Exporting them republishes
that document. Present in the library: Griffiths *Introduction to Quantum Mechanics*, Proakis &
Manolakis *DSP*, Gonzalez *Digital Image Processing*, Sedra–Smith *Microelectronic Circuits*, Ogata
*Modern Control Engineering*, Chapman *Electric Machinery*, Lathi *Modern Digital and Analog
Communication Systems*, Cheng *Engineering Electromagnetics* (**including its solutions manual**),
Beiser *Concepts of Modern Physics*, Heath *Scientific Computing*, Barnet *A Short Guide to Writing
About Art*, plus several dozen annotated IEEE/Elsevier/Frontiers papers.

Also excluded on the same grounds: instructor slide decks and syllabi, and **exam answer keys**
(`MT2_answerkey`, `Sample-midterm-solutions-2023`, `Electrical-Machinery-chapman-5th-2012-solution`).
This matches the rule already stated on the coursework page — own work only, no reposted solutions.

### Never publish — personal and confidential

These are in the same folder and must not be swept into any batch export that reaches the site:

- `TÜBİTAK BİLGEM İŞ SÖZLEŞMESİ` — employment contract
- `Vertraulichkeitsverpflichtung` — confidentiality undertaking
- `H3 Mietvertrag … Boran Aybak Kilic 2025-08-29 - 2025-10-02` — tenancy agreement
- `2224-D Programı Taahhütnamesi`, `BURS-DILEKCE-ORNEGI-ara-sinif-ogrenciler` — funding/scholarship undertakings
- `Personnel questionnaire ohne`, `Supplementary Questionnaire Academic`
- `Protection of Personal Data`, `Data Protection in Research`, `IT_Policy`, `Library_Regulations`,
  `leaflet General Equal Treatment Act` — institutional policy documents
- `Pompermaier_Andrea` — appears to be a third party's document
- `Voice 012`–`Voice 018` — audio recordings

## Mapping to the coursework page

Courses on the site that have Notability material:

| Course | Bundles (ink size) | Verdict |
|---|---|---|
| **ECE461** | HW03_sol 385 KB, HW02 318 KB, HW07 248 KB, HW08 237 KB, HW06 227 KB, HW05 130 KB, HW01 5 KB, 2 daily reviews | **Best candidate.** Real worked solutions in his hand across 7 problem sets. |
| **EE450** | HW4_Part2 1.75 MB, Homework_4 474 KB, syllabus 20 KB | Strong — two substantial worked homeworks. |
| **ECE449** | Lecture_1 45 KB | Thin — one lecture. |
| **ECE406** | Homework 12 KB, syllabus 5 KB | Thin. |
| **EE304** | reading list only, 5 KB | Instructor's document, nothing of his. |
| **PHYS380** | syllabus only, 6 KB | Instructor's document, nothing of his. |

No Notability material found for EE201, EE232, EE243, EE244, EE342, EE371, EE372, EE473, EE475,
PHYS302, or PHYS486.

### Courses with notes that are *not* on the coursework page

- **EE333** — 14 bundles (`lecture0`–`lecture13`), 110 KB–796 KB ink each. A full course.
- **EE351** — `notes1` 1.4 MB, `notes2` 2.6 MB + 1.8 MB, `notes3` 1.7 MB, `written-notes2`, HW3/4/5,
  syllabus. Substantial.
- **HTR 312** (art history) — two bundles plus his own MT1 study notes.

Both EE333 and EE351 are annotations on instructor slides, so the ink is his but the page underneath
isn't.

### Unlabelled lecture series (subject unidentified)

Boran mentioned labelling course notes as "course notes"; what's actually in the library are several
numbered series whose course is not in the filename:

- **`Lecture 1 - Harmonic Oscillator` … `Lecture 11 - Input-Output Formalism`** — unmistakably a
  **quantum optics** course: quantisation of the EM field, Fock and coherent states, squeezed states,
  beam splitters, field correlation functions, photon correlation measurements, nonlinear optics I/II,
  input–output formalism. Directly on-topic for the optical-quantum-information framing of the research
  page. Ink is light though (6–152 KB; heaviest are Lecture 11, 2, 3, 4), so these are mostly clean
  slide decks with light annotation.
- **`Lecture Notes 1` … `Lecture Notes 14`** — one course, unidentified.
- **`Lecture_2` … `Lecture_19`** — another course, unidentified. `Lecture_3` has 1.4 MB of ink.
- **`lecture1`/`lecture2`/`lecture3`** (lowercase) — a third, unidentified.
- **`Chapter2-SystemsOfLinearEquations` … `Chapter7-Interpolation`** — matches Heath *Scientific
  Computing*; a numerical-methods course. `Chapter4-EigenvalueProblems` has 1.1 MB of ink.
- **`L0_vector spaces and operators`** — a quantum mechanics course opener.

## Also found: MRSK working notes

Relevant to the research entry, not to coursework:

- `Multi Ratio Shift Keying (MRSK) for Molecullar Communicaiton.nbn` (and a URL-encoded duplicate)
- `Multi_Ratio_Shift_Keying__MRSK__Proposal_Draft-3.nbn`

Plus a large annotated molecular-communication literature set (~40 IEEE papers), which is how the
literature review for that paper was done.

## Suggested next step

1. Batch-export **only** the ECE461 and EE450 homework bundles from Notability as PDFs — these are his
   own solutions and map onto courses already on the site.
2. Separately, dump the 61 `thumb12x.png` thumbnails from the pure-handwriting bundles to identify what
   those dated notes actually cover. That's a cheap read-only operation and answers the one open
   question in this survey.
3. Leave everything PDF-backed alone unless a specific bundle turns out to be his own worked solution
   on a bare problem sheet.
