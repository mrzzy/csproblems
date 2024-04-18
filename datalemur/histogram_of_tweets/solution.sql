--
-- CSProblems
-- Datalemur
-- Histogram of Tweets
--
select c.tweet_bucket, count(c.*) as users_num
from
    (
        select user_id, count(*) as tweet_bucket
        from tweets
        where extract(year from tweet_date) = 2022
        group by user_id
    ) as c
group by c.tweet_bucket
;
