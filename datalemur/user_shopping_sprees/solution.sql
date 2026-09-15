--
-- CSProblems
-- Datalemur
-- DL1. User Shopping Sprees
--

WITH transactions_day AS (
  SELECT
    user_id,
    DATE_TRUNC('day', transaction_date) transaction_date
  FROM transactions
)
SELECT
  d1.user_id
FROM transactions_day d1
INNER JOIN transactions_day d2 
  ON d2.transaction_date = (d1.transaction_date + interval '1 day')
INNER JOIN transactions_day d3
  ON d3.transaction_date = (d1.transaction_date + interval '2 day')
GROUP BY d1.user_id
ORDER BY d1.user_id
