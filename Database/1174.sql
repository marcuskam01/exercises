select round(count(case when d.order_date = d.customer_pref_delivery_date then 1 else null end)/count(*)*100,2) as immediate_percentage
from Delivery d inner join 
(select customer_id, min(order_date) as earliest from Delivery 
group by customer_id) as sub
on d.customer_id = sub.customer_id and order_date = sub.earliest

