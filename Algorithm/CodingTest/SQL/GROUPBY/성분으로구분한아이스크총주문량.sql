select ii.ingredient_type as ingredient_tyep, sum(fh.total_order) as total_order
from first_half as fh
join icecream_info as ii on ii.flavor=fh.flavor
group by ii.ingredient_type
order by total_order