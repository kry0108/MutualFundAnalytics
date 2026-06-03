# Mutual Fund Analytics Project - Data Dictionary

## 1. Fund Master (01_fund_master.csv)

| Column Name        | Data Type | Description                 |
| ------------------ | --------- | --------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme code     |
| fund_house         | Text      | Mutual fund company name    |
| scheme_name        | Text      | Name of the scheme          |
| category           | Text      | Fund category               |
| sub_category       | Text      | Fund sub-category           |
| plan               | Text      | Direct/Regular plan         |
| launch_date        | Date      | Scheme launch date          |
| benchmark          | Text      | Benchmark index             |
| expense_ratio_pct  | Decimal   | Expense ratio percentage    |
| exit_load_pct      | Decimal   | Exit load percentage        |
| min_sip_amount     | Integer   | Minimum SIP amount          |
| min_lumpsum_amount | Integer   | Minimum lump sum investment |
| fund_manager       | Text      | Fund manager name           |
| risk_category      | Text      | Risk level                  |
| sebi_category_code | Text      | SEBI category code          |

Source: AMFI Mutual Fund Master Data

---

## 2. NAV History (02_nav_history.csv)

| Column Name | Data Type | Description      |
| ----------- | --------- | ---------------- |
| amfi_code   | Integer   | Scheme AMFI code |
| date        | Date      | NAV date         |
| nav         | Decimal   | Net Asset Value  |

Source: Historical NAV Data

---

## 3. AUM By Fund House (03_aum_by_fund_house.csv)

| Column Name    | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | Fund house name   |
| aum_lakh_crore | Decimal   | AUM in lakh crore |
| aum_crore      | Integer   | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |

Source: AMFI Industry Reports

---

## 4. Monthly SIP Inflows (04_monthly_sip_inflows.csv)

| Column Name               | Data Type | Description                      |
| ------------------------- | --------- | -------------------------------- |
| month                     | Text      | Reporting month                  |
| sip_inflow_crore          | Integer   | SIP inflow amount                |
| active_sip_accounts_crore | Decimal   | Active SIP accounts              |
| new_sip_accounts_lakh     | Decimal   | New SIP accounts                 |
| sip_aum_lakh_crore        | Decimal   | SIP AUM                          |
| yoy_growth_pct            | Decimal   | Year-over-year growth percentage |

Source: AMFI SIP Statistics

---

## 5. Category Inflows (05_category_inflows.csv)

| Column Name      | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Text      | Reporting month   |
| category         | Text      | Fund category     |
| net_inflow_crore | Decimal   | Net inflow amount |

Source: Category Wise Flow Data

---

## 6. Industry Folio Count (06_industry_folio_count.csv)

| Column Name         | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Text      | Reporting month |
| total_folios_crore  | Decimal   | Total folios    |
| equity_folios_crore | Decimal   | Equity folios   |
| debt_folios_crore   | Decimal   | Debt folios     |
| hybrid_folios_crore | Decimal   | Hybrid folios   |
| others_folios_crore | Decimal   | Other folios    |

Source: AMFI Folio Statistics

---

## 7. Scheme Performance (07_scheme_performance.csv)

| Column Name        | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Scheme AMFI code              |
| scheme_name        | Text      | Scheme name                   |
| fund_house         | Text      | Fund house                    |
| category           | Text      | Fund category                 |
| plan               | Text      | Scheme plan                   |
| return_1yr_pct     | Decimal   | 1 year return                 |
| return_3yr_pct     | Decimal   | 3 year return                 |
| return_5yr_pct     | Decimal   | 5 year return                 |
| benchmark_3yr_pct  | Decimal   | Benchmark return              |
| alpha              | Decimal   | Alpha ratio                   |
| beta               | Decimal   | Beta ratio                    |
| sharpe_ratio       | Decimal   | Sharpe ratio                  |
| sortino_ratio      | Decimal   | Sortino ratio                 |
| std_dev_ann_pct    | Decimal   | Annualized standard deviation |
| max_drawdown_pct   | Decimal   | Maximum drawdown              |
| aum_crore          | Integer   | Assets under management       |
| expense_ratio_pct  | Decimal   | Expense ratio                 |
| morningstar_rating | Integer   | Morningstar rating            |
| risk_grade         | Text      | Risk grade                    |

Source: Scheme Performance Dataset

---

## 8. Investor Transactions (08_investor_transactions.csv)

| Column Name        | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| investor_id        | Text      | Investor identifier     |
| transaction_date   | Date      | Transaction date        |
| amfi_code          | Integer   | Scheme code             |
| transaction_type   | Text      | SIP/Lumpsum/Redemption  |
| amount_inr         | Decimal   | Transaction amount      |
| state              | Text      | Investor state          |
| city               | Text      | Investor city           |
| city_tier          | Text      | City tier               |
| age_group          | Text      | Investor age group      |
| gender             | Text      | Investor gender         |
| annual_income_lakh | Decimal   | Annual income           |
| payment_mode       | Text      | Payment mode            |
| kyc_status         | Text      | KYC verification status |

Source: Investor Transaction Dataset

---

## 9. Portfolio Holdings (09_portfolio_holdings.csv)

| Column Name       | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Scheme code              |
| stock_symbol      | Text      | Stock symbol             |
| stock_name        | Text      | Stock name               |
| sector            | Text      | Industry sector          |
| weight_pct        | Decimal   | Portfolio weight         |
| market_value_cr   | Decimal   | Market value             |
| current_price_inr | Decimal   | Current stock price      |
| portfolio_date    | Date      | Portfolio reporting date |

Source: Portfolio Holdings Dataset

---

## 10. Benchmark Indices (10_benchmark_indices.csv)

| Column Name | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Index date           |
| index_name  | Text      | Benchmark index name |
| close_value | Decimal   | Closing index value  |

Source: Benchmark Index Dataset
