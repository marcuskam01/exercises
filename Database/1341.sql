with cte as (
select user_id, count(user_id) as rating_count from MovieRating m
group by user_id
), 
cte2 as (
select movie_id, avg(rating) as avg_rating from MovieRating m
where year(created_at) = 2020 and month(created_at) = 2
group by movie_id
)

(select u.name as results from cte
left join Users u on cte.user_id = u.user_id
order by cte.rating_count desc, u.name asc
limit 1)

union all

(select Movies.title as results from cte2
left join Movies on cte2.movie_id = Movies.movie_id
order by cte2.avg_rating desc, Movies.title asc
limit 1)