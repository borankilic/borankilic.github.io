---
title: Critical Dynamics in Brain Networks & Alzheimer's Disease
blurb: Simulating brain networks at their order–chaos phase transition, and asking whether Alzheimer's pushes the brain off criticality.
thumb: ../../assets/projects/brain-criticality-alzheimers/thumb.jpg
thumbAlt: Snapshots of a Greenberg–Hastings cellular automaton showing percolating clusters of activity
year: '2026'
role: Senior design project (EE 492) · with Aziz Umut Bakırcı · PI Prof. Burak Acar
venue: Boğaziçi University — B.S. thesis
tags: [Criticality, Connectomics, Statistical physics, Alzheimer's, DTI]
links:
  - { label: Final report (PDF), href: 'https://borankilic.github.io/pdfs/projects/brain/EE492_report.pdf' }
  - { label: Code (GitHub), href: 'https://github.com/borankilic/critical_brain' }
order: 2
featured: true
---

The **critical brain hypothesis** holds that large-scale neural networks self-organise near a continuous phase transition between ordered and chaotic dynamics — a regime that maximises information transmission and dynamic range. This senior design project asks a clinical question on top of that physics: **does Alzheimer's Disease break criticality, and can we measure how far a brain has drifted from it?**

## Approach

- **Data.** Subject-specific structural (DTI) and resting-state functional (fMRI) connectomes for 88 participants across three groups — Alzheimer's (AD, n=14), Mild Cognitive Impairment (MCI, n=43), and Subjective Cognitive Impairment (SCI, n=23) — parcellated into roughly 400 regions of interest.
- **Model.** We run a 3-state Greenberg–Hastings cellular automaton (quiescent → excited → refractory) on each subject's structural connectome and characterise the network's phase space with statistical-physics susceptibility metrics: the peak of the second-largest cluster size and the maximal variance of network activity, alongside a full mean-field fixed-point derivation with Jacobian-based stability analysis to back the simulation.
- **Validation.** Simulated functional connectivity matches empirical resting-state fMRI networks *most closely exactly at the structurally-defined critical threshold* (**T<sub>c</sub> ≈ 0.14–0.15**, agreeing across the cluster-size peak, the mutual-information peak, and the fMRI-similarity peak) — evidence that functional topology emerges from structural criticality. At criticality, the cluster-size distribution follows a power law with exponent **α ≈ 2.44**, consistent with genuinely scale-free dynamics rather than an arbitrary threshold effect.
- **Regional specificity.** By resting-state subnetwork, the simulated-vs-real connectivity correlation is highest in the **Somatomotor** subnetwork and the chi-squared distance smallest in **Visual Cortex** — the model-to-brain match isn't uniform across the cortex.

![Processing pipeline: DTI and rs-fMRI to structural and functional connectomes, Greenberg–Hastings simulation, and group-level classification.](../../assets/projects/brain-criticality-alzheimers/pipeline.png)

## A named phenomenon, not just a peak

The branching ratio σ (average descendants per active node) doesn't show a single sharp critical point across the threshold sweep so much as a **plateau near σ ≈ 1 over an extended range (~0.05–0.18)**. That flattened signature is a **Griffiths phase**, driven by structural heterogeneity in the connectome (following Moretti & Muñoz, 2013) — the brain glides along a broad ridge of near-critical behaviour rather than sitting at one knife-edge threshold.

## A new biomarker: Distance to Criticality

In AD patients the phase transition looks **flattened** — diminished, broader susceptibility peaks relative to SCI and MCI, consistent with a further-extended Griffiths phase and a shift toward a subcritical, disordered regime. To quantify this, we introduce **Distance to Criticality (DTC)**: how far a subject's optimal operating point sits from their own topological transition.

Classifying AD vs. SCI with a linear SVM (5-fold cross-validation) on a 17-feature set spanning critical-point location, operating-point fit, DTC, and Griffiths-phase shape, the **criticality-based feature subset reaches 77.8% accuracy** — clearly ahead of feature subsets built from pure goodness-of-fit metrics alone. The confusion matrix shows why that number needs a caveat: all 22 SCI subjects are correctly classified, but only 6 of 14 AD subjects (42.9%) are correctly identified as AD, with the other 8 misclassified as SCI. The false negatives concentrate specifically in **early- and mild-stage AD**, whose dynamical signatures overlap healthy aging — DTC as a biomarker is more of a "clearly diseased" detector than an early-warning one at this sample size.

A separate, unexplained finding: **four AD subjects** sit far below the rest of their cohort on every cluster/activity curve, with severe apparent structural disconnection, yet unremarkable clinical records and standard graph metrics (degree, clustering, betweenness) — the network seems to fragment before it even reaches the critical threshold, for reasons we don't have an explanation for yet.

![Cellular-automaton activity snapshots: clusters of excitation percolating through the simulated network near the critical regime.](../../assets/projects/brain-criticality-alzheimers/clusters.png)

The takeaway: Alzheimer's may drive a systemic shift of the brain's dynamical working point toward a subcritical, disordered phase, and "distance to criticality" is a candidate physics-informed marker of that shift — though with a small AD cohort (n=14) and sensitivity concentrated in more advanced disease, it needs validation on a larger, independent dataset before it's more than a promising signal.
