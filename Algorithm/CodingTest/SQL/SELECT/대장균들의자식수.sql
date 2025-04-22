select e.id, (select count(*) from ecoli_data where parent_id = e.id) as CHILD_COUNT
from ecoli_data as e
order by e.id