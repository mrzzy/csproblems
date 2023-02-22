--
-- CSProblems
-- Leetcode
-- 177. Nth Highest Salary
--

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
DETERMINISTIC
BEGIN
RETURN (
  WITH ranked_salary AS (
    SELECT
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM 
    Employee
  )
  SELECT (
    SELECT salary
    FROM ranked_salary
    WHERE salary_rank = N
    LIMIT 1
  )
);
END
