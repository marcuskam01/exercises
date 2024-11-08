with cte1 as (
    select * from Stadium where people >= 100
), cte2 as (
    select id, 
    lead(id, 1) over (order by id) as next1,
    lead(id, 2) over (order by id) as next2
    from cte1   
), cte3 as (
    select id from cte2
    where id = next1 - 1 and id = next2 - 2 
    union 
    select next1 from cte2
    where id = next1 - 1 and id = next2 - 2
    union
    select next2 from cte2
    where id = next1 - 1 and id = next2 - 2 
)

select * from Stadium s
where s.id in (select * from cte3)
order by visit_date asc