with
    user_actions_monthly as (
        select
            user_id,
            extract(month from event_date) as event_month,
            count(*) as event_count
        from user_actions
        where
            extract(year from event_date) = 2022
            and extract(month from event_date) between 6 and 7
        group by 1, 2
    ),
    user_actions_bimonthly as (
        select
            user_id,
            event_month,
            event_count as current_count,
            lag(event_count) over (
                partition by user_id order by event_month asc
            ) as previous_count
        from user_actions_monthly
    )
select event_month, count(user_id)
from user_actions_bimonthly
where
    event_month = 7
    and coalesce(current_count, 0) > 0
    and coalesce(previous_count, 0) > 0
group by 1
