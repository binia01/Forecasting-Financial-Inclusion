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
│   ├── ethiopia_fi_unified_data*.csv  # Main unified dataset
│   ├── reference_codes*.csv           # Valid codes reference
│   ├── Additional Data Points Guide*  # Enrichment guidance
│   └── data_enrichment_log.md         # Documentation of additions
├── notebooks/
│   └── 01_data_exploration_enrichment.ipynb  # Task 1 notebook
├── src/
│   └── __init__.py
├── dashboard/
│   └── app.py
├── models/
├── reports/
│   └── figures/
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

## 🔜 Upcoming Tasks

- **Task 3**: Build forecasting models for ACCESS and USAGE (2025-2027)
- **Task 4**: Create interactive dashboard presenting findings

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