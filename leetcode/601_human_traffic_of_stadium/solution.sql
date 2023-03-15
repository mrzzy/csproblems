--
-- CSProblems
-- Leetcode
-- 601. Human Traffic of Stadium
--
with
    hightraffic as (
        select
            id,
            visit_date,
            people,
            -- group ascending rows into the same group by subtracting row_number() 
            -- which monotonously increases.
            id - row_number() over (order by id asc) as ascending_group_id
        from stadium
        where people >= 100
    )
select id, visit_date, people
from hightraffic
where
    -- filter only large enough (>3 size) ascending groups
    ascending_group_id in (
        select ascending_group_id
        from hightraffic
        group by ascending_group_id
        having count(*) >= 3
    )
