select count(*) as FISH_COUNT, fn.FISH_NAME
from fish_info as fi
join fish_name_info as fn on fi.fish_type = fn.fish_type
group by fn.fish_name
order by FISH_COUNT desc