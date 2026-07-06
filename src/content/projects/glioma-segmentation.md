---
title: Classical Pipeline for Automated Glioma Segmentation
blurb: Segmenting brain tumors from multi-modal MRI using only classical image processing — no training data, no black boxes.
thumb: ../../assets/projects/glioma-segmentation/thumb.jpg
thumbAlt: Sagittal T2-weighted MRI slice of a human brain
year: '2026'
role: Course project (EE 475) · with Aziz Umut Bakırcı
venue: Boğaziçi University — Introduction to Image Processing
tags: [Image processing, Medical imaging, Morphology, BraTS 2021]
links:
  - { label: Report (PDF), href: 'https://borankilic.github.io/pdfs/projects/brats/EE475_report.pdf' }
order: 4
featured: false
---

Glioblastoma is the most aggressive class of primary brain tumor, and accurate segmentation of its sub-regions — necrotic core, enhancing tumor, peritumoral edema — is essential for quantifying tumor volume and planning radiotherapy. Modern approaches lean on deep U-Nets, which need large annotated datasets and are hard to interpret. **We asked how far a fully classical pipeline can get with no training data at all.**

## Pipeline

Built on the **BraTS 2021** dataset (multi-modal T1, T1CE, T2, FLAIR scans from 1,251 patients):

- **Preprocessing** — brain-mask extraction, N4 bias-field correction, z-score normalisation, and light Gaussian smoothing to tame intensity inhomogeneity.
- **Hierarchical segmentation** — instead of one classifier, we exploit the biological nesting of glioma layers (necrotic core ⊂ enhancing tumor ⊂ whole tumor) and iteratively restrict the domain: whole tumor → tumor core → necrotic core.
- **Geometry as a prior** — morphological operations and convex-hull seed constraints encode the tumor's shape explicitly, rather than learning it.

![Sagittal T2-weighted MRI slice from the BraTS dataset — the kind of multi-modal input the pipeline operates on.](../../assets/projects/glioma-segmentation/mri.png)

## Results

Across all patients the pipeline reaches a mean Dice of ≈0.72 on the whole tumor with no learned parameters — respectable for a purely classical method, and fully interpretable at every stage.

![Distribution of Dice scores across tumor sub-regions (whole tumor, enhancing, necrotic, core, edema) over all patients.](../../assets/projects/glioma-segmentation/dice.png)

The point isn't to beat deep learning — it's to show how much structure you can recover from geometry and physics-based contrast alone, with a method a clinician can actually inspect.
