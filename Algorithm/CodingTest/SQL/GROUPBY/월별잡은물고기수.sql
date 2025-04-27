select count(*) as FISH_COUNT, month(time) as MONTH
from fish_info
group by month(time)
having FISH_COUNT is not null
order by MONTH asc