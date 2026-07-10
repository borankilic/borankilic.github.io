---
title: Epileptic Seizure Detection with Wavelet Transforms
blurb: Decomposing EEG into brain-wave bands with the discrete wavelet transform, then separating seizure from non-seizure states.
thumb: ../../assets/projects/seizure-detection-wavelets/thumb.jpg
thumbAlt: EEG signal decomposed into delta, theta, alpha, beta, gamma and high-frequency wavelet bands
year: '2026'
role: Course project (EE 473) · with Aziz Umut Bakırcı
venue: Boğaziçi University — Introduction to Digital Signal Processing
tags: [Signal processing, Wavelets, EEG, Feature extraction]
links:
  - { label: Report (PDF), href: 'https://borankilic.github.io/pdfs/projects/epilepsy/EE473_report.pdf' }
  - { label: Code (GitHub), href: 'https://github.com/borankilic/wavelet_seizure_analysis' }
order: 5
featured: false
---

EEG is non-stationary: the frequency content of a seizure changes moment to moment, so a plain Fourier transform — which trades away all time information for frequency — is the wrong tool. The **wavelet transform** keeps both, and that is the core of this project: use it to pull an EEG recording apart into physiologically meaningful rhythms and detect seizures from how energy redistributes across them.

## Method

- **Denoising** — VisuShrink soft-thresholding on the wavelet coefficients, with a robust noise estimate, to clean the raw EEG before analysis.
- **Band decomposition** — a multi-level discrete wavelet transform (Daubechies family) maps DWT levels onto the classical EEG bands: delta, theta, alpha, beta, gamma, and a high-frequency residual.
- **Features & classification** — per-band energy and statistics form a feature vector; seizure vs non-seizure epochs are then separated by standard classifiers.

![EEG brain-wave decomposition via a db2 wavelet: delta, theta, alpha, beta, gamma and high-frequency bands, each with its energy.](../../assets/projects/seizure-detection-wavelets/bands.png)

## What separates seizures

Projecting the wavelet-derived features down to two dimensions shows the seizure and non-seizure populations occupying distinct regions of feature space — the redistribution of energy toward higher-frequency bands during seizures is visible even before a classifier is trained.

![Two-dimensional t-SNE projection of the EEG feature vectors, with seizure and non-seizure epochs forming separable clusters.](../../assets/projects/seizure-detection-wavelets/tsne.png)

The project doubles as a from-scratch derivation of the wavelet machinery — multiresolution analysis, the quadrature-mirror filter bank, the fast wavelet transform — grounding the detector in why the transform works, not just that it does.
