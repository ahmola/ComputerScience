# Window Function

집계 함수의 확장판

그룹화(Group By)하지않고, 전체 결과를 행별로 유지한 채 통째로 계산

OVER() 절을 동반해서 사용함

각 행마다 누적합, 순위, 이동평균, 이전/다음 행 비교 등에 쓰임

# 함수와 비교

기존 함수

    SELECT department_id, AVG(salary)
    FROM employees
    GROUP BY department_id;

윈도우 함수

    SELECT name, department_id, salary,
        AVG(salary) OVER (PARTITION BY department_id) AS avg_dept_salary
    FROM employees;