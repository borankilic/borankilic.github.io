---
title: Neural-Inspired Molecular Communication Networks
blurb: A swarm of simple diffusing nanomachines that computes collectively — and peaks in information capacity right at the edge of chaos.
thumb: ../../assets/projects/neural-inspired-molecular-communication/thumb.jpg
thumbAlt: 3D render of spherical nanomachine transceivers releasing molecules into a diffusive medium
year: '2026'
role: First author · with Prof. Özgür B. Akan (Koç University / University of Cambridge)
venue: MolCom 2026 — 10th Workshop on Molecular Communications
tags: [Molecular communication, Criticality, Complex systems, Information theory]
links:
  - { label: Paper (PDF), href: 'https://borankilic.github.io/pdfs/projects/molcom/MOLCOM26_paper.pdf' }
  - { label: Poster (PDF), href: 'https://borankilic.github.io/pdfs/projects/molcom/MOLCOM26_poster.pdf' }
order: 1
featured: true
---

Most work on molecular communication assumes *super-capable* individual nanomachines: perfect synchronisation, precise molecule counting, on-board signal processing far beyond anything current nanotechnology can build. This project asks the opposite question — **what if the agents are almost trivially simple, but there are many of them?**

The inspiration is the cortex. The brain does not compute because individual neurons are clever; it computes because millions of simple threshold-firing units interact collectively. We import that principle into the **Internet of Bio-Nano Things**: a decentralised network of spherical nanomachines that exchange information molecules through free diffusion, each firing according to a local threshold rule.

## What we did

- **Model.** Each agent is a Greenberg–Hastings excitable cellular automaton with three states — quiescent, excited, refractory. An agent fires when the molecules it absorbs in an interval exceed a threshold *T*, releasing its own molecules that diffuse to its neighbours.
- **Theory.** From the diffusion channel and the firing rule we derive closed-form, mean-field fixed-point equations for the steady-state population of excited agents, and validate them against stochastic simulation.
- **Result.** The network undergoes a **second-order phase transition** at a critical activation threshold. Both pairwise and collective **mutual information peak exactly at that critical point** — the system maximises information propagation and processing capacity at the "edge of chaos."

![3D render of the proposed nanomachine swarm communicating by diffusion, contrasted with traditional point-to-point molecular communication.](../../assets/projects/neural-inspired-molecular-communication/swarm.png)

The mean-field prediction matches simulation everywhere *except* near the transition — precisely where long-range correlations develop and the independence assumption breaks down. That gap is not a failure of the theory; it is the signature of criticality.

![Conference poster summarising the model, mean-field analysis, and the mutual-information peak at criticality.](../../assets/projects/neural-inspired-molecular-communication/poster.png)

## Why it matters

A single tunable parameter — the activation threshold — drives the whole network into a critical regime where collective computation emerges from diffusion alone. No complex individual agent required. It gives a quantitative, information-theoretic signature of "collective intelligence" that a real bio-nano network could, in principle, be engineered to sit on.
