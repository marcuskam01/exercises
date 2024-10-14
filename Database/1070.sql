select s1.product_id, s1.year as first_year, s1.quantity, s1.price from (select * from Sales) s1 inner join (select product_id, min(year) as first_year_temp from Sales group by product_id) s2
on s1.product_id = s2.product_id and s1.year = s2.first_year_temp

-- simpler solution
-- select product_id, year as first_year, quantity, price from sales
-- where (product_id, year) in (select product_id, min(year) from Sales group by product_id)


