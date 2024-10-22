select sub.person_name from (
select person_name, sum(weight) over (order by turn asc) as cum_weight from Queue) sub
where sub.cum_weight <= 1000
order by sub.cum_weight desc
limit 1