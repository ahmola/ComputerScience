# Transaction

데이터베이스에서 하나의 작업 단위로 처리되는 일련의 연산 묶음

성공하면 전부 적용되고, 하나라도 실패하면 전부 취소

일관성과 무결성을 보장하고 여러 쿼리를 원자적으로 처리

하나의 논리적 작업 단위라고 부른다

## ACID

Atoimicity : 원자성으로, 전부 성공하거나 전부 실패해야함

Consistency : 일관성으로, 트랜잭션 전후로 DB 상태는 무결해야 함

Isolation : 격리성으로, 동시에 여러 트랜잭션이 수행될 때 서로 간섭 X

Durability : 지속성으로, 일단 커밋되면서 시스템 장애에도 결과가 보존

## 트랜잭션 문법

기본 문법

    START TRANSACTION;

    -- 여러 쿼리 실행
    UPDATE accounts SET balance = balance - 10000 WHERE id = 1;
    UPDATE accounts SET balance = balance + 10000 WHERE id = 2;

    COMMIT; -- 전부 적용

    -- 또는 실패 시
    ROLLBACK; -- 전부 취소

요약 버전

    BEGIN;

    -- ... 쿼리들

    COMMIT;

Inno DB에서만 지원하는 특성이다.

보통 격리수준은 READ COMMITED나 REPEATABLE READ로 dirty read 방지를 위해 커밋된 값만 읽도록 함

너무 높은 수준의 격리는 성능 저하 유발

트랜잭션을 남발하면 락 경합, 성능 저하, 데드락 발생 가능성 증가

보통 백엔드 서비스에서 실패 가능성이 있고 실패 시 치명적인 작업들을 묶어서 처리할 때 사용함

Spring에서는 @transactional 어노테이션으로 처리 가능