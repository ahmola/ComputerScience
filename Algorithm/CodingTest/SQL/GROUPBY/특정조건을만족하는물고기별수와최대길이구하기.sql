-- sql에서 if문은 case when else end
select count(*) as FISH_COUNT, max(fi.length) as MAX_LENGTH, fi.FISH_TYPE
from (
    select fish_type,
    CASE
        WHEN length > 10 then length
        ELSE 10
    END as length
    from fish_info
) as fi
group by fi.fish_type
having avg(fi.length) >= 33
order by fish_type asc


