select count(*) as COUNT
from ecoli_data
where (genotype & 2 = False) and ((genotype & 1) or (genotype & 4))