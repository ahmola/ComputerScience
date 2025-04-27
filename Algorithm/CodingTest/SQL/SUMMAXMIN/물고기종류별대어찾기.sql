--select fo.id, fo.fish_name, fo.length
--from (select fi.id, fn.fish_name, fi.length
--    from fish_info as fi
--    join fish_name_info as fn on fi.fish_type=fn.fish_type) as fo
--join (select fish_name, max(length) as length
--    from (select fi.id as id, fn.fish_name as fish_name, fi.length as length
--        from fish_info as fi
--        join fish_name_info as fn on fi.fish_type=fn.fish_type) as ft
--    group by fish_name) as fm on fo.fish_name=fm.fish_name
--where fo.length=fm.length
--order by fo.id asc
-- 이렇게 풀 수 있지만 윈도우 함수로 쉽게 풀 수 있음
select id, fish_name, length
from (
    SELECT fi.id, fn.fish_name, fi.length,
           RANK() OVER (PARTITION BY fn.fish_name ORDER BY fi.length DESC) AS rk
    FROM fish_info fi
    JOIN fish_name_info fn ON fi.fish_type = fn.fish_type
) as ranked
where rk=1
order by id asc