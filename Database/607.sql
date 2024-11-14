select s.name from SalesPerson s
left join 
(select o.sales_id, c.name from Orders o  
left join Company c using(com_id)) sales_color
using(sales_id)
group by s.name
having sum(case when sales_color.name = 'RED' then 1 else 0 end) = 0