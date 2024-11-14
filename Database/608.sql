select id,
(case
    when p_id is null then 'Root'
    when id in (select p_id from Tree) and p_id in (select id from Tree) then 'Inner'
    else 'Leaf'
    end
) as type
from Tree