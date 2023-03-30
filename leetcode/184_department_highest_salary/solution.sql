--
-- CSProblems
-- Leetcode
-- 184. Department Highest Salary
--
select d.name department, e.name employee, salary salary
from employee e
inner join department d on d.id = e.departmentid
where
    salary
    = (select max(salary) from employee de where de.departmentid = e.departmentid)
