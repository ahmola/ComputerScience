# Procedure

SQL 로직을 함수처럼 저장하여 호출만 하면 실행되도록 만든 저장 루틴

서버에 저장되어 클라이언트가 CALL 명령으로 실행

트랜잭션 단위로 관리하거나 로직을 캡슐화

## 문법

    DELIMITER //

    CREATE PROCEDURE 프로시저명(IN 매개변수1 타입, OUT 매개변수2 타입)
    BEGIN
        -- SQL Query
    END //

    DELIMITER ;

호출 예시

    CREATE PROCEDURE GetUserById(IN user_id INT)
    BEGIN
        SELECT * FROM users WHERE id = user_id;
    END;

## 매개변수 타입

    CREATE PROCEDURE AddNum(IN num1 INT, IN num2 INT, OUT result INT)
    BEGIN
        SET result = num1 + num2;
    END;

- IN : 호출 시 값 전달(읽기 전용)
- OUT : 프로시저 실행 후 값 변환
- INOUT : 값 전달 + 결과 반영

## 내부 제어문

- 조건문

        IF 조건 THEN
        수행할 작업
        ELSEIF ...
        ...
        END IF;

- 반복문

        WHILE 조건 DO
        -- 반복 작업
        END WHILE;

- 루프 및 종료 조건

        LOOP
        -- 작업
        LEAVE label; -- 종료
        END LOOP;


## 장점

- 캡슐화 : 복잡한 로직을 모듈화

- 재사용성 : 반복되는 쿼리 저장

- 성능 : 한 번 컴파일 후 재사용

- 네트워크 비용 감소 : 일일이 클라이언트가 쿼리를 보낼 필요가 없음

- 보안 : 프로시저만 권한 부여 가능(테이블 직접 접근 제한)