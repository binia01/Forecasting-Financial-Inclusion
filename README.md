# Forecasting Financial Inclusion in Ethiopia

A forecasting system that tracks Ethiopia's digital financial transformation using time series methods.

## 📋 Project Overview

This project builds a forecasting system that predicts Ethiopia's progress on the two core dimensions of financial inclusion as defined by the World Bank's Global Findex:

- **ACCESS** — Account Ownership Rate
- **USAGE** — Digital Payment Adoption Rate

### Business Context

Ethiopia is undergoing rapid digital financial transformation:
- Telebirr has grown to over 54 million users since launching in 2021
- M-Pesa entered the market in 2023 and now has over 10 million users
- Interoperable P2P digital transfers have surpassed ATM cash withdrawals
- Yet only 49% of Ethiopian adults have a financial account (2024 Global Findex)

## 🚀 Project Setup

### Prerequisites
- Python 3.10+
- pip or conda

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Forecasting-Financial-Inclusion.git
cd Forecasting-Financial-Inclusion
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Required Packages
```
pandas
numpy
matplotlib
seaborn
```

## 📁 Project Structure

```
Forecasting-Financial-Inclusion/
├── data/
│   ├── raw/                           # Original starter dataset
│   ├── processed/                     # Enriched analysis-ready data
│   │   ├── event_indicator_matrix_refined.csv  # Calibrated impact estimates
│   │   └── forecast_2025_2027.csv     # Forecast table with CIs
│   ├── ethiopia_fi_unified_data*.csv  # Main unified dataset
│   ├── reference_codes*.csv           # Valid codes reference
│   ├── Additional Data Points Guide*  # Enrichment guidance
│   └── data_enrichment_log.md         # Documentation of additions
├── notebooks/
│   ├── 01_data_exploration_enrichment.ipynb  # Task 1 notebook
│   ├── 02_exploratory_data_analysis.ipynb    # Task 2 notebook
│   ├── 03_event_impact_modeling.ipynb        # Task 3 notebook
│   └── 04_forecasting_access_usage.ipynb     # Task 4 notebook
├── src/
│   └── __init__.py
├── dashboard/
│   └── app.py
├── models/
├── reports/
│   ├── figures/                       # All visualizations
│   ├── interim_report.md              # Interim submission
│   ├── eda_summary_report.md          # EDA findings
│   ├── event_impact_methodology.md    # Impact modeling methodology
│   └── forecast_executive_summary.md  # Forecast executive summary
├── tests/
│   └── __init__.py
├── requirements.txt
└── README.md
```

## 📊 Task 1: Data Exploration and Enrichment

### Objective
Understand the starter dataset and enrich it with additional data useful for forecasting ACCESS and USAGE indicators.

### Key Findings

#### Dataset Structure
The unified schema uses `record_type` to categorize data:
| Record Type | Count | Description |
|-------------|-------|-------------|
| observation | 30 | Measured values from surveys, reports, operators |
| event | 10 | Policies, product launches, market entries, milestones |
| target | 3 | Official policy goals (NFIS-II targets) |
| impact_link | 14 | Modeled relationships between events and indicators |

#### Account Ownership Trajectory (Core ACCESS Indicator)
| Year | Rate | Change |
|------|------|--------|
| 2011 | 14% | — |
| 2014 | 22% | +8pp |
| 2017 | 35% | +13pp |
| 2021 | 46% | +11pp |
| 2024 | 49% | +3pp |

#### Data Enrichment Summary
| Addition Type | Count | Examples |
|---------------|-------|----------|
| New Observations | 10 | 2011 baseline, bank branches, smartphone penetration |
| New Events | 6 | NPS Proclamation, CBE Birr launch, Agent Banking Directive |
| New Impact Links | 6 | Event-indicator relationships for ACCESS, USAGE, GENDER |

### Outputs
- 📓 `notebooks/01_data_exploration_enrichment.ipynb` — Full exploration and enrichment code
- 📄 `data/data_enrichment_log.md` — Detailed documentation of all additions
- 📊 `data/processed/ethiopia_fi_unified_data_enriched.csv` — Enriched dataset

## � Task 2: Exploratory Data Analysis

### Objective
Analyze patterns and factors influencing financial inclusion in Ethiopia.

### Key Insights

#### 1. The Account Ownership Paradox
Despite **65M+ mobile money registrations** (Telebirr 54.8M + M-Pesa 10.8M), account ownership only grew **+3pp** (46% → 49%) from 2021-2024.
- Mobile money-only users are rare (~0.5% of adults)
- Most MM users already have bank accounts (complementary, not substitute)
- Activity rate is only 66% (many dormant registrations)

#### 2. The Digital Crossover Milestone
**P2P transactions surpassed ATM withdrawals** in FY2024/25 — a historic first for Ethiopia:
- P2P: 128.3M transactions (+158% YoY)
- ATM: 119.3M transactions (+26% YoY)
- Crossover ratio: 1.08

#### 3. Persistent Gender Gap
- Account ownership gap: **18-20pp** (56% male vs 36% female)
- Women hold only **14%** of mobile money accounts
- Phone ownership gap: **24%** (86% male vs 65% female)

#### 4. Infrastructure as Leading Indicator
- 4G coverage doubled: 37.5% → **70.8%**
- Bottlenecks: Smartphone (24%), Mobile internet (26.9%)
- Traditional banking very sparse: 0.49 branches, 0.65 ATMs per 100k

#### 5. NFIS-II Target Gap
- Current: 49% | Target: 70% by 2025 | **Gap: 21pp**
- At current trajectory (+1pp/year), would reach 70% by 2046

### Data Quality Assessment
| Metric | Value |
|--------|-------|
| High confidence data | ~75% |
| Medium confidence data | ~25% |
| Temporal coverage | 2011-2025 |
| Core indicators sparse | Findex every 3 years |

### Outputs
- 📓 `notebooks/02_exploratory_data_analysis.ipynb` — Full EDA with visualizations
- 📄 `reports/eda_summary_report.md` — Key findings summary
- 📊 `reports/figures/` — All visualizations

## 🎯 Task 3: Event Impact Modeling

### Objective
Model how events (policies, product launches, infrastructure investments) affect financial inclusion indicators.

### Methodology

#### Functional Forms for Event Effects
| Form | Use Case | Example |
|------|----------|---------|
| **Step** | Permanent regulatory changes | NPS Proclamation |
| **Ramp** | Infrastructure buildout | 4G rollout |
| **Impulse-Decay** | Price shocks | FX reform |
| **S-Curve** | Technology adoption | Telebirr launch |

#### Comparable Country Evidence
Impact estimates derived from:
- **Kenya**: M-Pesa (+22% ownership), M-Shwari (first mobile credit)
- **Tanzania**: Vodacom M-Pesa (+15% ownership)
- **India**: Jan Dhan Yojana (+20% ownership), UPI (+25% digital payments)
- **Rwanda**: Agent banking (+12% ownership)
- **Bangladesh**: bKash (+18% ownership)

### Key Findings

#### Event-Indicator Association Matrix
Created comprehensive matrix showing estimated impact of **14 events** on **9 core indicators** across ACCESS, USAGE, AFFORDABILITY, and GENDER pillars.

#### Validation Results
| Indicator | Observed Δ | Predicted Δ | Error |
|-----------|------------|-------------|-------|
| Mobile Money Accounts | +4.75pp | +19.25pp | Over-predicted 4x |
| Account Ownership | +3pp | +10.25pp | Over-predicted 3x |
| 4G Coverage | +33.3pp | +34.5pp | Accurate (1.2pp error) |

**Key Insight**: Mobile money registrations ≠ survey-measured account ownership. Mobile money complements existing bank accounts rather than substituting for them.

#### Refined Impact Estimates
Applied adjustment factors based on validation:
- **ACCESS indicators**: Reduced by 50-70% (complementarity effect)
- **USAGE indicators**: Kept as-is (transaction data validates estimates)
- **4G Coverage**: Accurate, no adjustment needed

### Confidence Assessment
| Level | Count | Description |
|-------|-------|-------------|
| High | 4 | Validated, <30% error |
| Medium | 11 | Comparable evidence |
| Low | 5 | Theoretical only |

### Outputs
- 📓 `notebooks/03_event_impact_modeling.ipynb` — Full analysis notebook
- 📄 `reports/event_impact_methodology.md` — Detailed methodology documentation
- 📊 `data/processed/event_indicator_matrix_refined.csv` — Calibrated impact estimates
- 📈 `reports/figures/` — Impact visualizations (4 new figures)

## � Task 4: Forecasting Access and Usage

### Objective
Forecast Account Ownership (ACCESS) and Digital Payment Usage for 2025-2027.

### Methodology
Given sparse data (5 Findex data points over 13 years), we use:
1. **Trend Regression** - Linear model on historical Findex data (R² = 0.97)
2. **Event-Augmented Model** - Trend + expected event effects from Task 3
3. **Scenario Analysis** - Pessimistic, Base, and Optimistic scenarios

### Key Forecast Results

#### Account Ownership (ACCESS)
| Year | Trend Only | Base Scenario | Range (Pess - Opt) | 95% CI |
|------|------------|---------------|-------------------|--------|
| 2025 | 54.8% | 61.8% | 57.8% - 64.4% | [42.9%, 80.8%] |
| 2026 | 57.7% | 73.7% | 64.7% - 79.5% | [53.9%, 93.4%] |
| 2027 | 60.5% | 82.5% | 70.0% - 90.6% | [61.9%, 103.1%] |

#### Digital Payment Usage
| Year | Trend Only | Base Scenario | Range (Pess - Opt) | 95% CI |
|------|------------|---------------|-------------------|--------|
| 2025 | 48.6% | 59.6% | 53.3% - 63.6% | [35.8%, 83.4%] |
| 2026 | 52.9% | 82.9% | 66.4% - 93.4% | [59.1%, 106.8%] |
| 2027 | 57.3% | 105.3% | 79.1% - 122.0% | [81.5%, 129.1%] |

### Events with Largest Impact
| Event | ACCESS Impact | USAGE Impact | Confidence |
|-------|--------------|--------------|------------|
| Interoperability Full Launch (2026) | +4pp | +16pp | Low |
| EthioPay Instant Payment (2025) | +3pp | +15pp | Low |
| Telebirr continued growth | +6pp | +9pp | Medium |
| Fayda Digital ID rollout | +6pp | +2pp | Low |
| M-Pesa market penetration | +3pp | +6pp | Medium |

### NFIS-II Target Assessment
- **Target**: 70% account ownership by 2025
- **Current (2024)**: 49%
- **2025 Forecast (Base)**: 61.8%
- **Gap**: ~8pp
- **Conclusion**: ⚠️ Target is very unlikely to be met by 2025

### Key Uncertainties
1. **Data sparsity**: Only 5 Findex data points; CI width of ±21pp
2. **Event execution**: Interoperability & EthioPay timing uncertain
3. **Macro headwinds**: FX volatility, inflation may slow adoption
4. **Survey vs. Admin gap**: Mobile money registrations ≠ Findex ownership (4x gap)
5. **Gender gap**: Women's adoption trajectory could drag overall rates

### Outputs
- 📓 `notebooks/04_forecasting_access_usage.ipynb` — Forecasting notebook
- 📊 `data/processed/forecast_2025_2027.csv` — Forecast table with CIs
- 📄 `reports/forecast_executive_summary.md` — Executive summary
- 📈 `reports/figures/forecast_scenarios.png` — Scenario visualization
- 📈 `reports/figures/forecast_decomposition.png` — Trend vs event effects
- 📈 `reports/figures/nfis_target_gap.png` — Gap to NFIS-II target

## 🔜 Upcoming Tasks

- **Task 5**: Create interactive dashboard presenting findings

## 👥 Team

**Tutors**: Kerod, Mahbubah, Filimon

## 📅 Key Dates

- Challenge Introduction: January 28, 2026
- Interim Submission: February 1, 2026
- Final Submission: February 3, 2026

## 📚 Data Sources

- [World Bank Global Findex](https://www.worldbank.org/en/publication/globalfindex)
- [IMF Financial Access Survey](https://data.imf.org/?sk=E5DCAB7E-A5CA-4892-A6EA-598B5463A34C)
- [GSMA Intelligence](https://www.gsma.com/intelligence/)
- National Bank of Ethiopia
- Ethio Telecom Reports
- EthSwitch Annual Reports

---

*Selam Analytics — Financial Technology Consulting for Emerging Markets*