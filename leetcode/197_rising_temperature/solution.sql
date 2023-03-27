--
-- CSProblems
-- Leetcode
-- 197. Rising temperature
--
select today.id
from weather today
inner join
    weather yesterday on (yesterday.recorddate + interval 1 day) = today.recorddate
where today.temperature > yesterday.temperature
