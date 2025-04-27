-- concat을 하면 문자열이 되므로 연산이나 order by 시에 순수 데이터로만 따로 추출해서 써야함
select route as ROUTE,
        concat(round(sum(d_between_dist), 1), 'km') as TOTAL_DISTANCE,
        concat(round(avg(d_between_dist), 2), 'km') as AVERAGE_DISTANCE
from subway_distance
group by ROUTE
order by round(sum(d_between_dist), 1) desc