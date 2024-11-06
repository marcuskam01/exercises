with c as (select users_id, banned from Users where role = 'client'), 
d as (select users_id, banned from Users where role = 'driver'),

trip_ban as (select client_id, driver_id, status, request_at, c.banned as c_banned, d.banned as d_banned from Trips t
left join c on c.users_id = t.client_id
left join d on d.users_id = t.driver_id)

select request_at as 'Day', round(count(case when status != 'completed' then 1 else null end)/count(*),2) as 'Cancellation Rate' from trip_ban
where c_banned = 'No' and d_banned = 'No' and request_at between date("2013-10-01") and date("2013-10-03")
group by request_at