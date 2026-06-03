-- 1. Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by AMFI Code
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Monthly Average NAV
SELECT substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4. Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 7. Total Investments by Transaction Type
SELECT transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Top 5 Performing Funds (3 Year Return)
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 9. Number of Funds by Category
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 10. Average Expense Ratio by Category
SELECT AVG(expense_ratio_pct)
AS avg_expense_ratio
FROM fact_performance;