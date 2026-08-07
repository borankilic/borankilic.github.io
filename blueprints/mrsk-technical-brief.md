# MRSK — technical brief for the research entry

Written by Claude from the published paper on 2026-08-06. The IEEE Xplore PDF is **not** in this
repo (IEEE permits authors to post the accepted manuscript, not the Xplore version, and this repo
is public). Everything the research entry needs is below.

**Do not invent numbers, figures, or claims beyond this brief.** If a detail isn't here, leave it out.

## Citation

- **Title:** Multi Ratio Shift Keying (MRSK) Modulation for Molecular Communication
- **Authors:** Boran Aybak Kılıç, Özgür B. Akan (Fellow, IEEE)
- **Venue:** IEEE Transactions on Communications, vol. 73, no. 10, October 2025, p. 8873 ff. (13 pages)
- **DOI:** 10.1109/TCOMM.2025.3581006 → `https://doi.org/10.1109/TCOMM.2025.3581006`
- **Dates:** received 26 Dec 2024; revised 20 Apr 2025; accepted 8 Jun 2025; published 18 Jun 2025
- **Affiliation at time of work:** Center for neXt-generation Communications (CXC), Dept. of Electrical
  and Electronics Engineering, Koç University, Istanbul. Akan is also with the Internet of Everything
  (IoE) Group, Dept. of Engineering, University of Cambridge.
- **Funding:** AXA Research Fund (AXA Chair for Internet of Everything at Koç University)
- Boran is **corresponding author and first author.**

## The idea

Molecular communication (MC) sends information by releasing molecules that diffuse from transmitter
to receiver. Existing schemes encode into one of three properties: **concentration** (OOK, CSK, PAM),
**molecule type** (MoSK), or **release time** (RTSK). All of them suffer from inter-symbol
interference (ISI), because diffusion is slow and leaves molecules from previous symbols in the channel.

MRSK encodes information into the **ratios of the concentrations of several different molecule types** —
and specifically into *all possible ratios* within a set of molecules, rather than just one pair.
The channel is diffusion-based **without drift**.

### Why ratios

- **Channel-invariant expected value.** When the molecule types share the same diffusion coefficient,
  their spatiotemporal distributions track each other, so the *expected ratio* stays constant in space
  and time. The absolute counts decay with distance and time; the ratio does not.
- **Fixed-threshold detection.** That invariance permits a detection threshold that does **not** depend
  on channel conditions — no per-link estimation or retuning.
- **Well-suited to SIMO.** One transmitter can serve many receivers simultaneously without adjusting
  modulation/demodulation parameters per receiver — i.e. non-coherent detection across receivers.
- **Lighter distribution tails.** The PDF of a ratio of Gaussians has lighter tails than the individual
  Gaussians built from the same molecule count, giving more resilience to ISI and Gaussian noise.
- **Energy flexibility.** The same ratio can be produced with any total number of molecules, which
  matters in resource-limited environments.

### Biological motivation (as argued in the paper)

Ratio-based encoding has precedent in nature: rats can distinguish binary odour mixtures by the molar
ratio of components, recognising a mixture across varying absolute concentrations. In metabolic
networks, relative concentrations — e.g. the ATP/ADP balance in glycolysis — regulate enzyme activity
and pathway flux rather than absolute quantities.

## Relation to prior work

Ratio-based MC was introduced as **Isomer Ratio Shift Keying (IRSK)**, which used isomers as messenger
molecules but had limited statistical analysis. **Ratio Shift Keying (RSK)** later added a fuller
statistical model for ligand binding in stationary and mobile MC systems. Both encode using the ratio
of only **two** molecule types, and both assume symbol intervals long enough to ignore channel memory.

MRSK generalises past both limits: an M-ary scheme over all ratios of an arbitrary set of molecule
types, with channel memory accounted for.

## What the paper does

1. **Proposes MRSK** — generalises ratio-based MC to all possible ratios of a molecule set.
2. **Develops the mathematics of ratios of random variables**, focusing on **noncentral Gaussian**
   distributions, which is what lets the BER be derived precisely. The statistics of Gaussian ratio
   distributions in MC were largely unexplored before this.
3. **Introduces a flexible M-ary encoding** that adapts to different channel conditions.
4. **Evaluates analytically and by particle-based simulation** under varying channel conditions, and
   identifies the sources of error in the system model.
5. **Compares BER against the standard schemes** — OOK, CSK, PAM, MoSK, RTSK, and ADMC.

Index terms the authors chose: molecular communications, shift keying, modulation, bit error rate,
multi ratio shift keying, fixed threshold decoding, memory cancellation, ratio of random variables.

## Simulation parameters (verified from the paper)

| Quantity | Value |
|---|---|
| Transmitter–receiver distance *d* | 10 µm (swept over 8–12 µm in one study) |
| Receiver radius *r* | 5 µm |
| Diffusion coefficient *D* | 79.4 µm²/s |
| Channel memory length *L* | 5 symbols |

Detection complexity is reported as O(N(N−1)/2 + N + M(N−1)) for N molecule types and M-ary signalling.
Studies in the paper sweep BER against distance *d*, ratio range *Ω*, bit duration *t_b*, and *Q*.

## Results and conclusions

- MRSK **consistently beats** every conventional scheme compared, on BER.
- **Binary modulation with the fewest molecule types is optimal under moderate channel conditions.**
- **Higher-order modulation, or more molecule types, mitigates ISI** when bit times must be short —
  which is what makes MRSK suited to high-data-rate operation.
- There is a **convex relationship between ratio range and BER**, so the ratio spacing is a real design
  parameter to optimise, not a free choice.
- **Cost:** MRSK can require more molecules than conventional schemes, so it fits applications that
  demand high precision in environments where molecules are abundant.
- **Future work named by the authors:** threshold optimisation under varying channel conditions,
  resilience in diverse molecular networks, and integration into biological and nanotechnology-based
  communication platforms.

## Notes for writing the entry

- This is Boran's **first-author journal paper** — the most senior publication on the site. It already
  appears in the publications list on `src/pages/research/index.astro`; that entry should gain the DOI
  link rather than being duplicated.
- It is **distinct** from the MolCom 2026 work (`neural-inspired-molecular-communication`), which is
  about collective intelligence and criticality in nanomachine swarms. Same field and same advisor
  (Akan), different contribution. Cross-referencing them is reasonable; conflating them is not.
- There is no figure asset for MRSK in the repo. Do not fabricate one or reuse another entry's image.
