select hr.score, hr.emp_no, he.emp_name, he.position, he.email
from hr_employees as he
join (select sum(hg.score) as score, hg.emp_no as emp_no
    from hr_grade as hg
    where hg.year=2022
    group by hg.emp_no) as hr on hr.emp_no=he.emp_no
order by hr.score desc
limit 1