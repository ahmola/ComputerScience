--select month(car.start_date) as month, car.car_id, count(*) as records
--from car_rental_company_rental_history as car
--where car.car_id in (
--    select counts.car_id
--    from (
--        select car_id, count(*) as c
--        from car_rental_company_rental_history
--        where start_date between '2022-08-01' and '2022-10-31'
--        group by car_id
--        order by car_id
--    ) as counts
--    where c >= 5
--) and start_date between '2022-08-01' and '2022-10-31'
--group by month, car_id
--order by month, car_id desc
--최적화가 필요함
-- ========== 최척화된 코드 ==========
WITH rental_over_5 AS (
    SELECT car_id
    FROM car_rental_company_rental_history
    WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY car_id
    HAVING COUNT(*) >= 5
)

SELECT
    MONTH(start_date) AS MONTH,
    car_id,
    COUNT(*) AS RECORDS
FROM car_rental_company_rental_history
WHERE car_id IN (SELECT car_id FROM rental_over_5)
  AND start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY MONTH(start_date), car_id
ORDER BY MONTH, car_id DESC;