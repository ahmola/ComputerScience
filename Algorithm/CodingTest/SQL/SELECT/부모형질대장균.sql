-- 하나라도 갖는지 확인하는건 &, 만약 전부 포함하는지를 알고 싶으면 &연산 후 =로 피포함변수 확인
select child.id as ID, child.genotype as GENOTYPE, parent.genotype as PARENT_GENOTYPE
from ecoli_data as child
right join ecoli_data as parent on parent.id=child.parent_id
where parent.id is not null and (child.genotype & parent.genotype = parent.genotype)
order by child.id asc