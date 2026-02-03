
# Event Impact Modeling Methodology

## Overview
This document describes the methodology for modeling how events (policies, product launches, 
infrastructure investments) affect Ethiopia's financial inclusion indicators.

## 1. Functional Forms

We use four functional forms to represent how event effects propagate over time:

| Form | Formula | Use Case | Example |
|------|---------|----------|----------|
| Step | f(t) = M if t ≥ t₀+lag else 0 | Regulatory changes | NPS Proclamation |
| Ramp | f(t) = M × min(1, (t-t₀-lag)/ramp_period) | Infrastructure | 4G rollout |
| Impulse-Decay | f(t) = M × e^(-λ(t-t₀-lag)) | Price shocks | FX reform |
| S-Curve | f(t) = M / (1 + e^(-k(t-t₀-midpoint))) | Technology adoption | Telebirr |

Where:
- M = maximum effect magnitude
- t₀ = event time
- lag = delay before effect starts
- λ = decay rate
- k = steepness of S-curve

## 2. Impact Estimation Process

1. **Initial Estimates**: Derived from comparable country evidence (Kenya, Tanzania, India, Rwanda)
2. **Adjustment Factors**: Applied based on Ethiopia-specific context
3. **Validation**: Compared predicted vs observed changes (2021-2024)
4. **Refinement**: Calibrated estimates based on validation errors

## 3. Key Assumptions

1. **Additive Effects**: Multiple events' effects are summed (may underestimate interaction effects)
2. **Time Invariance**: Effect magnitude doesn't change based on when event occurs
3. **No Counterfactual**: Baseline assumes zero growth without events (may underestimate organic growth)
4. **Lag Certainty**: Assumed lag periods are fixed (in reality, highly variable)

## 4. Validation Results

| Indicator | Observed Δ | Predicted Δ | Error | Action |
|-----------|------------|-------------|-------|--------|
| Mobile Money Accounts | +4.75pp | +19.25pp | -14.5pp | Reduced by 50% |
| Account Ownership | +3pp | +10.25pp | -7.25pp | Reduced by 70% |
| 4G Coverage | +33.3pp | +34.5pp | -1.2pp | No change |

## 5. Limitations

1. **Data Sparsity**: Only 4-5 data points for core Findex indicators
2. **Confounding**: Cannot isolate event effects from other factors (economic growth, COVID-19)
3. **Measurement Gap**: Supply-side data (registrations) ≠ survey data (account ownership)
4. **Comparable Validity**: Kenya/India contexts may not fully translate to Ethiopia
5. **Forward Uncertainty**: Future events (EthioPay, Interoperability) have no validation data

## 6. Confidence Levels

| Level | Definition | Count |
|-------|------------|-------|
| High | Validated against observed data, <30% error | 4 |
| Medium | Based on comparable evidence, some validation | 11 |
| Low | Theoretical/literature-based, no validation | 5 |

## 7. Recommendations for Forecasting

1. Use refined (post-validation) estimates, not original
2. Apply wide confidence intervals (±50% for high confidence, ±100% for low)
3. Use S-curve for technology adoption events
4. For ACCESS indicators, use lower estimates due to complementarity effect
5. For USAGE indicators, original estimates appear reliable

---
Generated: 2026-02-03
