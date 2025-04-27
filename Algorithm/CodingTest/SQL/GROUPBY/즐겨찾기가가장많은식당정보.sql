select rest.food_type, rest.rest_id, rest.rest_name, rest.favorites
from (
    select *,
        row_number() OVER (partition by food_type
                           order by favorites desc) as rk
    from rest_info
) as rest
where rk = 1
order by rest.food_type desc