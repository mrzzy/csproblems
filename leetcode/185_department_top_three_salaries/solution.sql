--
-- CSProblems
-- Leetcode
-- 185. Department Top Three Salaries
--
with
    employeesalaryranked as (
        select
            salary,
            name,
            departmentid,
            dense_rank() over (
                partition by departmentid order by salary desc
            ) as salaryrank
        from employee
    )

select
    department.name as department,
    employeesalaryranked.name as employee,
    employeesalaryranked.salary as salary
from employeesalaryranked
inner join department on department.id = employeesalaryranked.departmentid
where salaryrank in (1, 2, 3)
