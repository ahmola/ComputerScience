-- where로 조건을 차근차근 하나씩 줄여나가기
select item_id, item_name, rarity
from item_info
where item_id in (select item_id
                from item_tree
                where parent_item_id in (select item_id
                                        from item_info
                                        where rarity='RARE'))
order by item_id desc