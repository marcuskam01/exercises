with cte1 as (
    select s.student_id, s.student_name, sj.subject_name
    from Students s
    cross join Subjects sj

), cte2 as (
    select student_id, subject_name, count(*) as attended_exams
    from Examinations e
    group by e.student_id, e.subject_name
)

select cte1.student_id, cte1.student_name, cte1.subject_name, coalesce(cte2.attended_exams,0) as attended_exams from cte1
left join cte2
on (cte1.student_id = cte2.student_id 
and cte1.subject_name = cte2.subject_name)
order by cte1.student_id, cte1.subject_name