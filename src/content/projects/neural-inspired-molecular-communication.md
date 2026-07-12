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

- **Model.** Each agent is a Greenberg–Hastings excitable cellular automaton with three states — quiescent, excited, refractory. An agent fires when the molecules it absorbs in an interval exceed an activation threshold *T*, releasing *N₀* molecules that diffuse to its neighbours as fully-absorbing receivers. Simulated: N = 100 agents Poisson-distributed in a sphere of radius 20 µm, receiver radius 4 µm, diffusion coefficient D = 79.4 µm²/s, 100 molecules per emission, a channel memory of 5 time steps, and a 1 s time slot.
- **Theory.** From the diffusion channel's analytically-derived absorption probability and the firing rule, we derive closed-form, mean-field fixed-point equations for the steady-state population of excited agents (solved via under-relaxed fixed-point iteration), and validate them against stochastic simulation.
- **Result.** The network undergoes a **second-order phase transition at a critical activation threshold T<sub>c</sub> = 550.0** molecules, separating a sub-critical "saturation" phase (threshold below ≈450, noise-dominated) from a super-critical "silence" phase (threshold above ≈600, activity dies out). Mean population activity falls from about 25 of 100 agents active in the sub-critical phase to near zero above the transition, while the standard deviation of activity — the susceptibility — peaks sharply right at T<sub>c</sub>. Both pairwise and collective **mutual information peak at that same threshold** — the system maximises information propagation and processing capacity at the "edge of chaos."

![3D render of the proposed nanomachine swarm communicating by diffusion, contrasted with traditional point-to-point molecular communication.](../../assets/projects/neural-inspired-molecular-communication/swarm.png)

The mean-field prediction matches simulation everywhere *except* near the transition — precisely where long-range correlations develop and the independence assumption breaks down. That gap is not a failure of the theory; it is the signature of criticality: the absolute error between theoretical and simulated excitation probability diverges specifically and only in the neighbourhood of T<sub>c</sub>.

![Conference poster summarising the model, mean-field analysis, and the mutual-information peak at criticality.](../../assets/projects/neural-inspired-molecular-communication/poster.png)

## Why it matters

A single tunable parameter — the activation threshold — drives the whole network into a critical regime where collective computation emerges from diffusion alone. No complex individual agent required. It gives a quantitative, information-theoretic signature of "collective intelligence" that a real bio-nano network could, in principle, be engineered to sit on.

**Open ends.** The diffusive channel carries significant memory (inter-symbol interference), so even identical initial configurations can diverge dynamically — links are stochastic, not fixed weights as in a static graph network. Channel noise itself is not purely a nuisance: via stochastic resonance it can enhance weak-signal detection rather than degrade it. Natural next steps we haven't done yet: a finite-size-scaling treatment of the correlations that build up near T<sub>c</sub>, extending the model to heterogeneous (non-isotropic) tissue diffusion, and defining a formal information-theoretic channel capacity for the network rather than relying on mutual information as a proxy.
