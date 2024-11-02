select employee_id from (
select * from Employees where salary < 30000) temp
where temp.manager_id not in (select employee_id from Employees)
order by employee_id asc