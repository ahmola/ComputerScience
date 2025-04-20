select book_id, date_format(published_date, "%Y-%m-%d") as published_date
from book
where published_date like "2021%" and category="인문"
order by published_date asc