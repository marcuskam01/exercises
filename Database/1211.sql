select q.query_name, round(sum(q.rating/q.position)/count(*),2) as quality,round(count(case when q.rating < 3 then 1 else null end)/count(*)*100,2) as poor_query_percentage from Queries q
where query_name is not null 
group by q.query_name