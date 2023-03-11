--
-- CSProblems
-- Leetcode
-- 180. Consecutive Numbers
--
with
    num_window as (
        select
            lag(num, 2) over () as first_num,
            lag(num, 1) over () as second_num,
            num as third_num
        from logs
    )
select distinct first_num as consecutivenums
from num_window
where first_num = second_num and second_num = third_num;
