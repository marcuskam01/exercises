select sub.name from (
select e1.name, count(e1.id) as tally from Employee e1 join Employee e2 on e1.id = e2.managerId group by e1.id) sub
where sub.tally >= 5