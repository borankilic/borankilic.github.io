---
title: NV-Center Magnetometry
blurb: Building and characterising a diamond nitrogen-vacancy magnetometer — reading magnetic fields from the fluorescence of atomic defects.
thumb: ../../assets/projects/nv-center-magnetometry/thumb.jpg
thumbAlt: Optically detected magnetic resonance spectrum showing the characteristic double-dip, raw and reconstructed
year: '2025'
role: Experimental research · TÜBİTAK BİLGEM Quantum Technologies
venue: TÜBİTAK BİLGEM UEKAE — Quantum Technologies department
tags: [Quantum sensing, NV centers, ODMR, Lock-in detection, Experiment]
links:
  - { label: Code (GitHub), href: 'https://github.com/borankilic/NV_center' }
order: 3
featured: true
researchOnly: true
---

Nitrogen-vacancy (NV) centers are atomic defects in diamond whose fluorescence depends on the local magnetic field, which makes a diamond a remarkably sensitive, room-temperature magnetometer. I worked on this at the **Quantum Technologies department of TÜBİTAK BİLGEM** — a hands-on experimental project to build the optical and microwave setup and characterise how well it can actually measure a field.

## What the experiments cover

- **ODMR spectroscopy.** Sweeping a microwave tone across the ≈2.87 GHz NV resonance (I run the setup at a center frequency of **2.874 GHz**) while collecting photoluminescence gives the optically detected magnetic resonance (ODMR) spectrum. Under a strong bias field we resolve the full **hyperfine structure**: **8 sets of 3 peaks (24 peaks total)**, one triplet — from the *m*<sub>I</sub> = −1, 0, +1 nitrogen spin states — per Zeeman-split branch, per crystallographic NV orientation. At a weaker bias field of 1.3 mT, peaks from orientation pairs overlap and only **12 peaks** are resolvable.
- **Lock-in detection.** Frequency-modulating the microwave (FM deviation 5.3 MHz, rate 18 kHz) and demodulating the photodiode signal with an SR860 lock-in amplifier (time constant 30 ms, laser power 330 mW) converts the ODMR dip into a voltage that tracks the field linearly.
- **Signal recovery.** Raw ODMR sweeps are noisy; I compared moving-average, envelope, exponential and quadrature filtering, with a Hilbert-like envelope (quadrature approximation) method recovering the cleanest peak structure. Switching from a Handyscope HS5 (500 MSa/s) to an Agilent DSO7054B oscilloscope (2 GSa/s, 4× the sampling rate) also measurably cleaned up the raw peaks — some of the noise was the digitizer, not the physics.

![Raw ODMR sweep (left) and the reconstructed spectrum (right) showing the characteristic double-dip resonance after denoising.](../../assets/projects/nv-center-magnetometry/odmr.png)

## Characterising the instrument

- **Dynamic range.** Sweeping a controlled Helmholtz-coil field (monitored against a Fluxmaster fluxgate reference) maps the linear regime of the response curve and where it saturates. The usable linear response spans **[−40 µT, +20 µT]** — a 60 µT window — with an intrinsic offset of about **−10 µT** from unaccounted external fields, giving a **maximum measurable field of 30 µT** before the curve saturates.
- **Tuning for sensitivity.** An FM deviation of **1.2 MHz** gives the steepest zero-crossing slope of the demodulated dip — the most sensitive detection point — found by sweeping deviation and comparing slopes. Sweeping laser diode current similarly showed **300 mA gives the best (lowest) noise floor**, by both a time-domain estimator (effective noise bandwidth f<sub>ENBW</sub> ≈ 1/(4τ) ≈ 8.33 Hz at τ = 30 ms) and a frequency-domain estimator (mean of the sensitivity spectrum from 1–33.3 Hz). The exact sensitivity values in nT/√Hz live only in the recorded chart images, not in my notes, so I'm leaving them out here rather than guess.
- **Detector timing.** Cross-correlating the reference and signal photodetector traces during a manually-stepped power transient shows the reference PD lagging the signal PD by **1.3 ms**, attributed to a difference in optical path length between the two arms.
- **Averaging trade-offs.** Driving an alternating square-wave field (100 Hz, via Helmholtz coils) and averaging the lock-in output over 1000 cycles sharply narrows the confidence interval and removes high-frequency noise — but only works for fields slow enough that the averaging window doesn't wash out the waveform, and even at the 30 µs lock-in time constant used, the output ramps between the square wave's levels rather than tracking its edges instantaneously. Both are the usual smoothing-vs-bandwidth trade-off, just made concrete on real hardware.

![Lock-in emission spectrum over time, showing the modulated photoluminescence signal used to extract the magnetic field.](../../assets/projects/nv-center-magnetometry/emission.png)

Alongside the measurements I built a Python pipeline for preprocessing the raw detector data and a machine-learning experiment for extracting field estimates from the ODMR spectra.

## Honest limitations

The hyperfine measurements relied on a strong bias field from **10 stacked neodymium bar magnets** on the translation stage — a deliberately non-ideal choice: the metal stage leaked flux and the bars' own field is heterogeneous, so the bias field's exact direction and magnitude weren't well controlled. A Helmholtz coil would be the right way to do this, but the coil setup available couldn't reach the needed field strength at the voltages on hand. I also never tracked down the source of a persistent low-frequency drift on the signal photodetector — my best guess is thermal, but it's unconfirmed.
