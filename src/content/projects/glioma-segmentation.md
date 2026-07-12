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
  - { label: Code (GitHub), href: 'https://github.com/borankilic/brats' }
order: 4
featured: false
---

Glioblastoma is the most aggressive class of primary brain tumor, and accurate segmentation of its sub-regions — necrotic core, enhancing tumor, peritumoral edema — is essential for quantifying tumor volume and planning radiotherapy. Modern approaches lean on deep U-Nets, which need large annotated datasets and are hard to interpret. **We asked how far a fully classical pipeline can get with no training data at all.**

## Pipeline

Built on the **BraTS 2021** dataset (multi-modal T1, T1CE, T2, FLAIR scans from 1,251 patients, each 240×240×155 voxels at 1 mm³ isotropic resolution, co-registered and skull-stripped):

- **Preprocessing** — brain-mask extraction, N4ITK bias-field correction, z-score normalisation, and light Gaussian smoothing to tame intensity inhomogeneity.
- **Hierarchical segmentation** — instead of one classifier, we exploit the biological nesting of glioma layers (necrotic core ⊂ enhancing tumor ⊂ whole tumor) and iteratively restrict the domain, entirely in 3D rather than slice-by-slice (slice-wise processing loses inter-slice correlations that matter for connectivity):
  - **Whole tumor** from a FLAIR/T2 percentile threshold, cleaned up with morphological opening to detach the tumor from skull/gray-matter bridges, then largest-connected-component selection and closing.
  - **Enhancing tumor** from a gamma-corrected T1CE−T1 enhancement map, thresholded with a **region-restricted Otsu threshold computed only inside the whole-tumor mask** — plus a boundary-subtraction step specifically to strip out false-positive "enhancement" from cortical CSF near the brain-mask edge.
  - **Necrotic core** from the T1CE hypointensity, seeded inside a 3D convex hull of the enhancing-tumor mask and grown with Seeded Region Growing or Marker-Controlled Watershed (the default); if the result comes out under 5,000 voxels, it falls back to the convexified enhancing-tumor mask minus the enhancing tumor itself.
  - **Tumor core** = necrotic core ∪ enhancing tumor; **edema** = whole tumor − tumor core.

![Sagittal T2-weighted MRI slice from the BraTS dataset — the kind of multi-modal input the pipeline operates on.](../../assets/projects/glioma-segmentation/mri.png)

## Results

Tested on **12 subjects held out from the BraTS validation set** (the 1,251-patient figure above is the source dataset the pipeline draws on, not the evaluation size), the pipeline reaches:

| Region | Dice | Hausdorff-95 (mm) |
|---|---|---|
| Whole tumor | **0.839 ± 0.085** | 11.11 ± 15.26 |
| Tumor core | **0.846 ± 0.086** | 7.54 ± 12.17 |
| Enhancing tumor | 0.802 ± 0.091 | 6.27 ± 11.54 |
| Necrotic core | 0.742 ± 0.178 | 7.31 ± 9.70 |
| Edema | 0.688 ± 0.150 | 14.15 ± 15.39 |

Tumor core actually scores marginally higher than whole tumor. Necrotic core and edema are the lowest-scoring, most variable regions — consistent with them having the subtlest intensity gradients and least regular shapes, which is exactly where a geometry-driven pipeline is weakest. With n=12, treat these as indicative rather than population-level numbers.

![Distribution of Dice scores across tumor sub-regions (whole tumor, enhancing, necrotic, core, edema) over all patients.](../../assets/projects/glioma-segmentation/dice.png)

## Where it fails

The clean numbers above hide some specific, recurring failure modes:

- **Multifocal glioblastoma** — disjoint tumor "islands" get mishandled, since largest-connected-component selection discards every island but the biggest, violating the pipeline's own nested-hierarchy assumption.
- **Ground-truth artifacts** — the human-annotated labels often lack slice-to-slice continuity, producing jagged "non-biological staircase" boundaries; some of the Dice penalty is inconsistent ground truth, not a wrong segmentation.
- **Seed-selection leakage** — highly irregular or non-convex enhancing-tumor rings loosen the convex-hull seed constraint for necrotic-core growing, letting seeds land in non-tumor tissue and the region-growing step "leak" outward.

The point isn't to beat deep learning — it's to show how much structure you can recover from geometry and physics-based contrast alone, with a method a clinician can inspect at every stage, while being honest about where a geometric prior runs out of road.
