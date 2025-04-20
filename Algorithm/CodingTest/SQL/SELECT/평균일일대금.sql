select round(AVG(car.daily_fee),0) as AVERAGE_FEE
from car_rental_company_car as car
where car.car_type='SUV'