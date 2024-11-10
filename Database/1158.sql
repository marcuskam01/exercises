select user_id as buyer_id, join_date, coalesce(o_in_2019,0) as orders_in_2019 from Users u
left join 
(select buyer_id, count(*) as o_in_2019 from Orders o
where year(order_date) = 2019
group by buyer_id) b_count
on u.user_id = b_count.buyer_id