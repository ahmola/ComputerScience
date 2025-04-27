-- regexp '|' 를 사용하면 여러 개를 한꺼번에 조건 검색가능
select car_type, count(*) as cars
from car_rental_company_car
where options regexp '가죽시트|열선시트|통풍시트'
group by car_type
order by car_type asc