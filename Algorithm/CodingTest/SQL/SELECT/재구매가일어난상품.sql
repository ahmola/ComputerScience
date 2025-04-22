-- group by는 속성에 맞춰 중복되는 데이터를 하나로 묶는 역할, having은 이렇게 묶인 데이터를 조건에 맞춰서 필터링
select user_id, product_id
from online_sale
group by user_id, product_id
having count(*) > 1
order by user_id asc, product_id desc