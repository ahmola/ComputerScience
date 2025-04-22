-- &연산으로 int형 자료들의 비트연산이 가능함. 그러므로 join으로 묶어서
-- 필터링을 진행함
SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) > 0
WHERE S.NAME IN ('Python', 'C#')
ORDER BY D.ID;