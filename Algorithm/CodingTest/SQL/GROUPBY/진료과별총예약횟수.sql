-- 취소여부를 어쩌라는건지는 써놓지도 않으면 어쩌라는건지;;
select mcdp_cd as 진료과코드, count(*) as 5월예약건수
from appointment
where apnt_ymd like '2022-05-%'
group by mcdp_cd
order by 5월예약건수 asc, 진료과코드 asc