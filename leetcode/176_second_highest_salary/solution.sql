--
-- CSProblems
-- Leetcode
-- 176. Second Highest Salary
--

SELECT (
    SELECT DISTINCT
        salary
    FROM
        Employee
    ORDER BY salary DESC
    LIMIT 1
    OFFSET 1
) SecondHighestSalary
