#!/usr/bin/env python3
"""
Publication-style figures for single-sided-cavity reflection readout.

FIG A (cavity_response.png):
    Reflection of a single-sided cavity, r(Delta) = 1 - kappa_ext / (i*Delta + kappa/2),
    kappa = kappa_ext + kappa_int, vs normalised detuning Delta/kappa, for three
    coupling ratios eta = kappa_ext/kappa: over-coupled (0.8), critical (0.5),
    under-coupled (0.2).

FIG B (mzi_transfer.png):
    Unbalanced Mach-Zehnder readout of a differential phase: complementary
    output intensities I+/- and fringe visibility vs arm-delay mismatch.

Run standalone:
    python3 make_figures.py

Requires matplotlib >= 3.9, numpy. No LaTeX (mathtext only).
"""

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------------------------
# Paper-style rcParams
# --------------------------------------------------------------------------
plt.rcParams.update(
    {
        "font.family": "serif",
        "mathtext.fontset": "dejavuserif",
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 7.5,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.3,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
        "xtick.minor.visible": True,
        "ytick.minor.visible": True,
        "xtick.major.size": 3.5,
        "ytick.major.size": 3.5,
        "xtick.minor.size": 2.0,
        "ytick.minor.size": 2.0,
        "legend.frameon": False,
        "savefig.dpi": 350,
        "figure.dpi": 150,
        "axes.grid": False,
    }
)

# Okabe-Ito colourblind-safe palette
BLACK = "#000000"
BLUE = "#0072B2"
VERMILLION = "#D55E00"

HERE = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# Physics: single-sided cavity reflection
# --------------------------------------------------------------------------
def cavity_r(x, eta):
    """Reflection coefficient r(x) for normalised detuning x = Delta/kappa
    and coupling ratio eta = kappa_ext/kappa. Denominator normalised so that
    kappa = 1: D = i*x + 1/2.
    """
    D = 1j * x + 0.5
    return 1.0 - eta / D


def run_sanity_checks():
    """Numerically verify the two physics claims the figure is built on:
    (1) |r|^2 is identical for eta and 1-eta (over/under-coupled degeneracy);
    (2) unwrapped phase winds by ~2*pi across resonance when over-coupled,
        and returns to ~its starting value when under-coupled.
    Returns a dict of numbers for reporting.
    """
    eta_over, eta_crit, eta_under = 0.8, 0.5, 0.2

    # (1) intensity degeneracy, evaluated on the plotted range
    x_plot = np.linspace(-6, 6, 4000)
    I_over = np.abs(cavity_r(x_plot, eta_over)) ** 2
    I_under = np.abs(cavity_r(x_plot, eta_under)) ** 2
    max_abs_diff = float(np.max(np.abs(I_over - I_under)))

    # (2) phase winding, evaluated on a wide domain so both ends have
    # relaxed back to the free-propagation value (r -> 1, phase -> 0 mod 2pi)
    x_wide = np.linspace(-2000, 2000, 8000)
    phase_over = np.unwrap(np.angle(cavity_r(x_wide, eta_over)))
    phase_under = np.unwrap(np.angle(cavity_r(x_wide, eta_under)))
    span_over_pi = (phase_over[-1] - phase_over[0]) / np.pi
    span_under_pi = (phase_under[-1] - phase_under[0]) / np.pi

    return {
        "max_abs_intensity_diff": max_abs_diff,
        "phase_span_over_pi": span_over_pi,
        "phase_span_under_pi": span_under_pi,
    }


# --------------------------------------------------------------------------
# FIG A: cavity_response.png
# --------------------------------------------------------------------------
def make_fig_cavity_response(outpath):
    eta_over, eta_crit, eta_under = 0.8, 0.5, 0.2

    x = np.linspace(-6, 6, 4000)
    r_over = cavity_r(x, eta_over)
    r_crit = cavity_r(x, eta_crit)
    r_under = cavity_r(x, eta_under)

    I_over = np.abs(r_over) ** 2
    I_crit = np.abs(r_crit) ** 2
    I_under = np.abs(r_under) ** 2

    phi_over = np.unwrap(np.angle(r_over)) / np.pi
    phi_crit = np.unwrap(np.angle(r_crit)) / np.pi
    phi_under = np.unwrap(np.angle(r_under)) / np.pi

    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(3.4, 4.6), sharex=True, gridspec_kw={"height_ratios": [1, 1], "hspace": 0.08}
    )

    # --- panel (a): reflected intensity ---
    ax1.plot(x, I_crit, color=BLACK, ls="-", label=r"critical ($\kappa_\mathrm{ext}/\kappa=0.5$)", zorder=2)
    ax1.plot(x, I_over, color=BLUE, ls="--", label=r"over-coupled ($\kappa_\mathrm{ext}/\kappa=0.8$)", zorder=3)
    ax1.plot(
        x,
        I_under,
        color=VERMILLION,
        ls="none",
        marker="o",
        markersize=3.0,
        markevery=80,
        markerfacecolor="none",
        markeredgewidth=0.8,
        label=r"under-coupled ($\kappa_\mathrm{ext}/\kappa=0.2$)",
        zorder=4,
    )

    ax1.set_ylabel(r"$|r|^2$")
    ax1.set_ylim(-0.03, 1.05)
    ax1.legend(loc="lower right", handlelength=2.2, borderaxespad=0.4)

    # --- panel (b): reflection phase ---
    ax2.plot(x, phi_crit, color=BLACK, ls="-", zorder=2)
    ax2.plot(x, phi_over, color=BLUE, ls="--", zorder=3)
    ax2.plot(
        x,
        phi_under,
        color=VERMILLION,
        ls="none",
        marker="o",
        markersize=3.0,
        markevery=80,
        markerfacecolor="none",
        markeredgewidth=0.8,
        zorder=4,
    )

    ax2.set_xlabel(r"$(\omega-\omega_0)/\kappa$")
    ax2.set_ylabel(r"$\arg(r)/\pi$")
    # y-limits must contain the full over-coupled excursion (it winds to ~-2pi);
    # clipping it would hide the very effect this figure exists to show.
    ax2.set_xlim(-6, 6)
    _phi_lo = min(phi_over.min(), phi_under.min(), phi_crit.min())
    _phi_hi = max(phi_over.max(), phi_under.max(), phi_crit.max())
    _pad = 0.12 * (_phi_hi - _phi_lo)
    ax2.set_ylim(_phi_lo - _pad, _phi_hi + _pad)

    # terse mathematical annotation marking the 2pi winding of the
    # over-coupled curve (no explanatory prose)
    ax2.annotate(
        "",
        xy=(0.75, phi_over[np.argmin(np.abs(x - 0.75))]),
        xytext=(-0.75, phi_over[np.argmin(np.abs(x + 0.75))]),
        arrowprops=dict(arrowstyle="<->", color=BLUE, lw=0.8, shrinkA=0, shrinkB=0),
    )
    ax2.text(0.0, -0.15, r"$2\pi$", color=BLUE, ha="center", va="top", fontsize=8)

    for ax, lab in ((ax1, "(a)"), (ax2, "(b)")):
        ax.text(-0.20, 1.03, lab, transform=ax.transAxes, fontsize=10, fontweight="bold", va="bottom", ha="left")

    fig.align_ylabels([ax1, ax2])
    fig.savefig(outpath, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# --------------------------------------------------------------------------
# FIG B: mzi_transfer.png
# --------------------------------------------------------------------------
def make_fig_mzi_transfer(outpath):
    V0 = 0.9  # peak visibility used for the transfer-function panel

    dphi_pi = np.linspace(-2, 2, 2000)  # differential phase, units of pi
    dphi = dphi_pi * np.pi
    I_plus = 1.0 + V0 * np.cos(dphi)
    I_minus = 1.0 - V0 * np.cos(dphi)

    dtau = np.linspace(-3, 3, 2000)  # arm delay mismatch, units of tau_c
    V = np.exp(-(dtau**2))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 2.7))

    # --- panel (a): complementary MZI outputs ---
    ax1.plot(dphi_pi, I_plus, color=BLACK, ls="-", label=r"$I_+$", zorder=3)
    ax1.plot(dphi_pi, I_minus, color=VERMILLION, ls="--", label=r"$I_-$", zorder=3)

    for q in (-1.5, -0.5, 0.5, 1.5):
        ax1.axvline(q, color=BLUE, ls=":", lw=0.8, zorder=1)

    ax1.text(
        0.5,
        1.98,
        r"$\Delta\varphi=\pi/2$",
        color=BLUE,
        fontsize=7,
        ha="center",
        va="top",
    )

    ax1.set_xlabel(r"$\Delta\varphi/\pi$")
    ax1.set_ylabel(r"$I_\pm$ (norm.)")
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(0, 2.05)
    ax1.set_xticks([-2, -1, 0, 1, 2])
    ax1.legend(loc="upper right", handlelength=2.0, borderaxespad=0.3, ncol=1)

    # --- panel (b): fringe visibility vs arm delay mismatch ---
    ax2.plot(dtau, V, color=BLACK, ls="-", zorder=3)
    e_inv = np.exp(-1.0)
    ax2.axhline(e_inv, color=VERMILLION, ls=":", lw=0.8, zorder=1)
    ax2.plot([-1, 1], [e_inv, e_inv], marker="o", markersize=3.0, ls="none", color=VERMILLION, zorder=3)
    ax2.text(1.35, e_inv, r"$1/e$", color=VERMILLION, fontsize=7, va="center", ha="left")

    ax2.set_xlabel(r"$\Delta\tau/\tau_c$")
    ax2.set_ylabel(r"$V$")
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(0, 1.05)

    for ax, lab in ((ax1, "(a)"), (ax2, "(b)")):
        ax.text(-0.18, 1.05, lab, transform=ax.transAxes, fontsize=10, fontweight="bold", va="bottom", ha="left")

    fig.tight_layout()
    fig.savefig(outpath, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# --------------------------------------------------------------------------
if __name__ == "__main__":
    checks = run_sanity_checks()
    print("Sanity checks:")
    print(f"  max |I_over - I_under|            = {checks['max_abs_intensity_diff']:.3e}")
    print(f"  over-coupled unwrapped phase span = {checks['phase_span_over_pi']:+.6f} pi")
    print(f"  under-coupled unwrapped phase span = {checks['phase_span_under_pi']:+.6f} pi")

    fig_a_path = os.path.join(HERE, "cavity_response.png")
    fig_b_path = os.path.join(HERE, "mzi_transfer.png")

    make_fig_cavity_response(fig_a_path)
    make_fig_mzi_transfer(fig_b_path)

    for p in (fig_a_path, fig_b_path):
        size_kb = os.path.getsize(p) / 1024.0
        print(f"wrote {p}  ({size_kb:.1f} KB)")
