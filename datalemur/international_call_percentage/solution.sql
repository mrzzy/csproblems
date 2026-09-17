--
-- CSProblems
-- Datalemur
-- DL3. International Call Percentage
--


SELECT
    ROUND(SUM(
        CASE
            WHEN i1.country_id <> i2.country_id THEN 1
            ELSE 0
        END
    ) * 100.0 / COUNT(*), 1) AS international_calls_pct
FROM phone_calls p
INNER JOIN phone_info i1 ON i1.caller_id = p.caller_id
INNER JOIN phone_info i2 ON i2.caller_id = p.receiver_id
