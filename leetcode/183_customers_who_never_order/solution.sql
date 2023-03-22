--
-- CSProblems
-- Leetcode
-- 183. Customers Who Never Order
--
select name customers
from customers c
where not exists (select 1 from orders where customerid = c.id)
