-- 겹치는 구간을 구하려면 시작점은 최대값 이하로, 끝점은 최소값 이상으로 나와야된다
select cc.car_id as CAR_ID,
    cc.car_type as CAR_TYPE,
    floor(30*(cc.daily_fee*(1-dp.discount_rate/100))) as FEE
from car_rental_company_car as cc
join car_rental_company_discount_plan as dp
    on dp.duration_type='30일 이상' and dp.car_type=cc.car_type
where (cc.car_type='세단' or cc.car_type='SUV')
    and cc.car_id not in (
        select car_id
        from car_rental_company_rental_history
        where start_date <= '2022-11-30' and end_date >= '2022-11-01'
    )
    and 30*(cc.daily_fee*(1-dp.discount_rate/100)) >= 500000
    and 30*(cc.daily_fee*(1-dp.discount_rate/100)) < 2000000
order by FEE desc, CAR_TYPE asc, CAR_ID desc