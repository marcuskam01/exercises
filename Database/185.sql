select d.name as Department, rnk_table.name as Employee, rnk_table.salary as Salary from (
    select name, salary, departmentId, dense_rank() over (partition by departmentId order by salary desc) as rnk from Employee
) rnk_table
left join Department d on rnk_table.departmentId = d.id
where rnk_table.rnk <= 3