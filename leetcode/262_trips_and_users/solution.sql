--
-- CSProblems
-- Leetcode
-- 262. Trips and Users
--
select
    request_at as day,
    round(sum(status <> 'completed') / count(*), 2) as "Cancellation Rate"
from trips
where
    -- only count valid trips records are made by unbanned users
    driver_id in (select users_id from users where banned = 'No')
    and client_id in (select users_id from users where banned = 'No')
    and request_at between '2013-10-01' and '2013-10-03'
group by request_at
