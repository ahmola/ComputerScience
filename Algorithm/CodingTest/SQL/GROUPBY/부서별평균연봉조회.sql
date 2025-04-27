select he.dept_id as DEPT_ID, hd.dept_name_en as DEPT_NAME_EN, round(avg(he.sal), 0) as AVG_SAL
from hr_employees as he
join hr_department as hd on hd.dept_id=he.dept_id
group by he.dept_id
order by AVG_SAL desc