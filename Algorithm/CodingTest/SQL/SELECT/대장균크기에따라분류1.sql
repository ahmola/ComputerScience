(select id, 'LOW' as size
from ecoli_data
where size_of_colony <= 100

union

select id, 'MEDIUM' as size
from ecoli_data
where size_of_colony > 100 and size_of_colony <= 1000

union

select id, 'HIGH' as size
from ecoli_data
where size_of_colony > 1000)
order by id