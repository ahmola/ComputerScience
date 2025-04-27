select name, count(*) as count
from animal_ins
group by name
having name is not null and count >= 2
order by name