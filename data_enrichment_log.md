# Data Enrichment Log

## Ethiopia Financial Inclusion - Task 1: Data Exploration and Enrichment

**Date**: 2026-02-01  
**Collected By**: Task1_Enrichment  
**Notebook**: `notebooks/01_data_exploration_enrichment.ipynb`

---

## 1. Dataset Overview

### Original Dataset Statistics:
| Dataset | Records | Description |
|---------|---------|-------------|
| ethiopia_fi_unified_data.csv | 43 | Main data (observations, events, targets) |
| Impact_sheet.csv | 14 | Impact links between events and indicators |
| reference_codes.csv | 66 | Valid codes for all categorical fields |

### Records by Type (Original):
| Record Type | Count | Description |
|-------------|-------|-------------|
| observation | 30 | Measured values from surveys, reports, operators |
| event | 10 | Policies, product launches, market entries, milestones |
| target | 3 | Official policy goals (NFIS-II targets) |

---

## 2. Data Schema Understanding

### Key Design Principle:
Events are **NOT** pre-assigned to pillars. Their effects on specific indicators are captured through `impact_link` records. This keeps the data unbiased.

### How to Query:
- **Events** → `category` field indicates type (product_launch, policy, etc.)
- **Observations** → `pillar` field indicates dimension measured (ACCESS, USAGE, etc.)
- **Impact Links** → `parent_id` connects to event, `related_indicator` specifies affected indicator

---

## 3. Temporal Coverage Analysis

### Account Ownership (ACC_OWNERSHIP) - Core ACCESS Indicator:
| Year | Value | Source | Notes |
|------|-------|--------|-------|
| 2014 | 22% | Global Findex 2014 | First available in original data |
| 2017 | 35% | Global Findex 2017 | +13pp growth |
| 2021 | 46% | Global Findex 2021 | +11pp growth |
| 2024 | 49% | Global Findex 2024 | +3pp growth (slowdown) |

**Gap Identified**: Missing 2011 baseline (14%) - ADDED in enrichment

### Key Events Timeline:
- 2012: Agent Banking Directive (NEW)
- 2017: CBE Birr Launch (NEW)
- 2019: Telecom Liberalization Announcement (NEW)
- 2020: National Payment System Proclamation (NEW)
- 2021-05: Telebirr Launch, Safaricom License
- 2022-08: Safaricom Commercial Launch
- 2023-08: M-Pesa Launch
- 2024-01: Fayda Digital ID Rollout
- 2024-07: FX Liberalization
- 2025: EthioPay, M-Pesa Interoperability

---

## 4. Enrichment Summary

### 4.1 New Observations Added (10 records)

| Record ID | Indicator | Value | Date | Source | Confidence | Notes |
|-----------|-----------|-------|------|--------|------------|-------|
| REC_0034 | ACC_OWNERSHIP | 14% | 2011-12-31 | Global Findex 2011 | high | First Findex baseline - critical for time series |
| REC_0035 | ACC_BANK_BRANCHES | 0.49 per 100k | 2023-12-31 | IMF FAS | high | Traditional banking infrastructure |
| REC_0036 | ACC_ATM_DENSITY | 0.65 per 100k | 2023-12-31 | IMF FAS | high | ATM infrastructure indicator |
| REC_0037 | ACC_MOBILE_INTERNET | 26.9% | 2024-01-01 | DataReportal | high | Key enabler for mobile financial services |
| REC_0038 | ACC_SMARTPHONE | 24% | 2024-01-01 | GSMA Intelligence | medium | Critical for app-based mobile money |
| REC_0039 | ACC_ADULT_POP | 71M | 2024-12-31 | World Bank | high | Denominator for per-capita metrics |
| REC_0040 | USG_DIGITAL_PAYMENT | 35% | 2024-11-29 | Global Findex 2024 | high | Core USAGE indicator |
| REC_0041 | USG_WAGE_RECEIPT | 15% | 2024-11-29 | Global Findex 2024 | medium | Formal financial system integration |
| REC_0042 | ACC_OWNERSHIP (urban) | 62% | 2024-11-29 | Global Findex 2024 | medium | Urban disaggregation |
| REC_0043 | ACC_OWNERSHIP (rural) | 38% | 2024-11-29 | Global Findex 2024 | medium | Rural disaggregation |

### 4.2 New Events Added (6 records)

| Record ID | Event | Category | Date | Source | Confidence | Rationale |
|-----------|-------|----------|------|--------|------------|-----------|
| EVT_0011 | National Payment System Proclamation | regulation | 2020-01-01 | NBE | high | Legal framework enabling mobile money |
| EVT_0012 | CBE Birr Mobile Money Launch | product_launch | 2017-05-01 | CBE | high | Pre-Telebirr mobile banking service |
| EVT_0013 | Agent Banking Directive | regulation | 2012-01-01 | NBE | high | Enabled agency banking model |
| EVT_0014 | Telecom Sector Liberalization Announcement | policy | 2019-06-01 | Government | high | Preceded Safaricom entry |
| EVT_0015 | Safaricom Telecom License Awarded | market_entry | 2021-05-22 | ECA | high | Major step in ending telecom monopoly |
| EVT_0016 | Telebirr Super App Feature Expansion | product_launch | 2023-06-01 | Ethio Telecom | medium | Expanding beyond P2P to ecosystem |

### 4.3 New Impact Links Added (6 records)

| Record ID | Event | Affected Indicator | Direction | Magnitude | Lag | Evidence |
|-----------|-------|-------------------|-----------|-----------|-----|----------|
| IMP_0015 | NPS Proclamation | ACC_MM_ACCOUNT | increase | high (+20%) | 18 mo | Tanzania |
| IMP_0016 | CBE Birr | ACC_OWNERSHIP | increase | low (+3%) | 12 mo | Empirical |
| IMP_0017 | Telebirr Super App | USG_DIGITAL_PAYMENT | increase | medium (+10%) | 6 mo | Kenya |
| IMP_0018 | Agent Banking Directive | ACC_OWNERSHIP | increase | medium (+8%) | 24 mo | Kenya |
| IMP_0019 | Telecom Liberalization | ACC_4G_COV | increase | high (+30%) | 36 mo | Rwanda |
| IMP_0020 | NFIS-II | GEN_GAP_ACC | decrease | medium (-5pp) | 24 mo | Theoretical |

---

## 5. Data Quality Notes

### Confidence Levels Used:
- **high**: Primary source, verified, official data
- **medium**: Secondary source, cross-referenced
- **low**: Single source, unverified

### Known Data Gaps:
1. **Sparse Account Ownership**: Only 5 data points (2011, 2014, 2017, 2021, 2024)
2. **Missing intermediary years**: No annual observations for core Findex indicators
3. **Limited gender disaggregation**: Only available for some indicators

### Recommendations for Future Enrichment:
1. Add more infrastructure data from EthSwitch (POS terminals, QR merchants)
2. Collect agent network density data from banks
3. Add regional disaggregation where available
4. Include more proxy variables for interpolation

---

## 6. Output Files

### Saved to `data/processed/`:
| File | Records | Description |
|------|---------|-------------|
| ethiopia_fi_unified_data_enriched.csv | 59 | Merged main data + new observations + new events |
| impact_links_enriched.csv | 20 | Merged impact links + new impact links |

### Visualization saved to `reports/figures/`:
- `record_type_distribution.png`
- `pillar_distribution.png`
- `temporal_coverage.png`
- `enriched_data_summary.png`

---

## 7. Schema Compliance Verification

All new records follow the unified schema:
- ✅ Observations have `pillar` set, `category` empty
- ✅ Events have `category` set, `pillar` empty
- ✅ Impact links have `parent_id` linking to event, `pillar` derived from affected indicator
- ✅ All required fields populated with valid reference codes
- ✅ Source URLs provided where available
- ✅ Collection metadata (collected_by, collection_date) added

---

## 8. Next Steps

1. **Task 2**: Analyze patterns and relationships in the enriched data
2. **Task 3**: Build forecasting models for ACCESS and USAGE (2025-2027)
3. **Task 4**: Create interactive dashboard presenting findings

---

*Last updated: 2026-02-01*
