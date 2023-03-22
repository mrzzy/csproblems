--
-- CSProblem
-- Hackerrank
-- 15 Days of Learning SQL
--
select unique_hackers_per_day.submission_date, n_unique, hacker_id, name
from
    (
        select submission_date, h.hacker_id, h.name
        from
            (
                select max_submission_day.submission_date, min(hacker_id) hacker_id
                from
                    (
                        select submission_date, max(n_submission) as max_submission
                        from
                            (
                                select submission_date, hacker_id, count(*) n_submission
                                from submissions
                                group by submission_date, hacker_id
                            ) n_submission_by_hacker_day
                        group by submission_date
                    ) max_submission_day
                inner join
                    (
                        select submission_date, hacker_id, count(*) n_submission
                        from submissions
                        group by submission_date, hacker_id
                    ) n_submission_by_hacker_day
                    on n_submission_by_hacker_day.submission_date
                    = max_submission_day.submission_date
                where n_submission = max_submission
                group by max_submission_day.submission_date
            ) top_hacker_per_day_min_id
        inner join hackers h on h.hacker_id = top_hacker_per_day_min_id.hacker_id
    ) top_hacker_per_day
inner join
    (
        select submission_date, count(distinct hacker_id) as n_unique
        from submissions daily
        where hacker_id IN (
            -- hackers that make a least 1 submission per day of competition
            select hacker_id
            from submissions
            where submission_date <= daily.submission_date
            group by hacker_id
            having count(distinct submission_date) >= extract(day from daily.submission_date)
        )
        group by submission_date
    ) unique_hackers_per_day
    on top_hacker_per_day.submission_date = unique_hackers_per_day.submission_date
order by unique_hackers_per_day.submission_date asc
