# Truong Xuan Khanh & Truong Quynh Hoa — Sources

---

## "Entropy Collapse: A Universal Failure Mode of Intelligent Systems — Exact Phase Transition Analysis, First-Order Discontinuity, and Two Universality Classes" (2025)

**Access status:** open  
**URL:** https://arxiv.org/abs/2512.12381  
**Authors:** Truong Xuan Khanh, Truong Quynh Hoa  
**Submitted:** December 13, 2025; revised March 13, 2026

*Note: The source transcript attributes these findings to "Ken Hou and Houa" — a phonetic rendering of the Vietnamese names Khanh and Hoa. The paper's exact formula α_c = 1/(1−β) and proof of first-order phase transition are a precise match for the claims attributed in the transcript.*

### Core argument

Feedback-amplified adaptive systems fail via **entropy collapse** — a sudden, irreversible contraction of effective state space that is qualitatively different from the gradual critical transitions assumed by conventional complexity science. Standard early-warning signals (rising autocorrelation, rising variance) cannot detect entropy collapse because the transition is first-order (discontinuous): the system appears stable at every point, including immediately before collapse.

The mechanism: when feedback amplification exceeds the system's capacity to regenerate novelty, effective entropy drops catastrophically. The threshold is exact and mathematically derivable: **α_c = 1/(1−β)**, where α is feedback amplification rate and β is adaptive coupling. Below the threshold the system self-corrects; above it, collapse is sudden and irreversible for Class 1 systems.

The framework unifies three superficially unrelated phenomena: AI model collapse (language models degrading when trained on their own outputs), institutional rigidity in economics, and evolutionary genetic bottlenecks.

### Key claims

1. **First-order phase transition, not second-order:** Entropy collapse is discontinuous — the entropy order parameter jumps abruptly at the critical point (Δm₀ = 0.698) with measurable hysteresis (ΔH_hyst ≈ 2.73 nats). Standard warning signals remain finite even at the last moment before collapse.
2. **Exact threshold formula:** α_c(β) = 1/(1−β), derived from spectral analysis of the Multiplicative-Weights operator's Jacobian. This is an exact result, not an approximation.
3. **Two universality classes:** Class 1 (convex feedback, e.g. power-law functions) → irreversible collapse. Class 2 (linear feedback) → reversible dynamics. The curvature parameter κ = f″(1/N) determines which class a system belongs to.
4. **Universal relaxation exponent:** Class 1 systems show ν = 1 relaxation (transcritical bifurcation scaling) with R² = 0.9997 in simulation — indicating universality across different implementation details.
5. **Empirical validation in neural networks:** A two-layer autoregressive transformer (SmallGPT, 50-token vocabulary) confirmed the theoretical predictions: ΔH_hyst^NN = 2.92 nats and ν^NN = 1.14 ± 0.13 (R² = 0.977), consistent with Class 1 behaviour.

### Methodology

- **Theoretical:** Spectral analysis of the Multiplicative-Weights operator Jacobian; bifurcation theory (transcritical bifurcation analysis); phase transition theory with entropy order parameter
- **Empirical:** Neural network experiments on SmallGPT across 92 experimental conditions with 8 random seeds per condition; entropy dynamics measured and compared against theoretical predictions
- **Framework:** Mathematics / complex systems theory; applies physics-style phase transition formalism to adaptive computation
