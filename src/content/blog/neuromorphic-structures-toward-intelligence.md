---
title: Neuromorphic Structures Toward Intelligence
description: Why intelligence might be as much about the substrate as the algorithm, and what "computing at the edge of chaos" buys you.
date: 2026-05-18
tags: [Intelligence, Complexity, Neuromorphic, Criticality]
---

There's a habit of thought I can't shake. Whenever I look at something intelligent, I want to know what its parts are doing, not just what the whole is computing. A neuron is almost embarrassingly simple. It integrates inputs, and past a threshold, it fires. That's it. And yet a few billion of them, wired the right way, write poetry and prove theorems and fall in love. The gap between the part and the whole is, to me, one of the most interesting problems in science.

## Intelligence might be a property of the substrate

Most of modern AI treats intelligence as an *algorithm* — a function you approximate with enough parameters and data. That view has been spectacularly productive, and I don't want to argue against it. But it quietly assumes the substrate doesn't matter: run the same weights on a GPU or a warehouse of abacuses and you'd get the same mind.

Neuromorphic thinking pushes back. It says the *physics* of the computing medium — how units are coupled, how signals propagate, how energy dissipates — is not an implementation detail but part of what makes the computation possible at all. The brain isn't a von Neumann machine that happens to be wet. Its memory and its processing live in the same place, it runs on ~20 watts, and it never stops being a dynamical system.

## The edge of chaos keeps showing up

Here's the thread that ties a lot of my work together. Take a network of simple excitable units and turn a single knob — call it the coupling strength, or the firing threshold. Turn it one way and activity dies out; the network is silent, ordered, subcritical. Turn it the other way and activity explodes; every unit drags its neighbours along, and the whole thing seizes into noise, supercritical.

In between there is a sharp transition. And right at that transition — the *critical point* — something remarkable happens:

- correlations become long-ranged, so a local event can influence the whole network;
- the dynamic range is maximised, so the system responds to both faint and strong inputs;
- and, in the models I've worked with, **mutual information peaks** — the network transmits and stores the most information exactly there.

> Compute too far into order and nothing propagates. Compute too far into chaos and nothing is stable. The interesting regime — the one that looks like *information processing* — is the knife's edge between them.

I saw this first in a molecular-communication network of nanomachines, where tuning one threshold drove a genuine second-order phase transition with information capacity peaking at the critical point. I saw it again, from the clinical side, in simulated brain networks, where Alzheimer's looks like a brain sliding *off* criticality into a subcritical, disordered phase. Different substrates, same physics.

## What I take from this

I don't think "criticality" is a magic word that explains intelligence. Plenty of critical systems are just sand piles. But I do think the direction is right: if you want to understand — or build — a system that computes richly with cheap parts, you should be asking where its phase transitions are and whether it's sitting near one.

That reframes the engineering question in a way I find hopeful. You don't need every unit to be smart. You need many simple units, the right coupling, and a way to hold the collective near its critical point. The intelligence isn't *in* the parts. It's in the regime.

That's the idea I keep circling back to, and most of what I write here will be me trying to take it apart.
