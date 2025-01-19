SQL(Structured Query Language) : 관계형 데이터베이스 표준 언어

    데이터 정의어(Data Definition Language) : DB구조 정의, DB 객체 생성, 수정, 삭제

    데이터 조작어(Data Manipulation Language) : DB 데이터 관리, 입력, 수정, 삭제, 검색

    데이터 제어어(Data Control Language) : DB 관리 및 통제, DB 백업 및 복원, 사용자 등록과 권한 관리

MYSQL 기준 SQL 사용법

    CREATE USER '아이디'@'호스트(사용자 접속지점, %는 모든 IP)' IDENTIFIED BY '비밀번호'; 
    => 호스트에서 접속하는 '아이디'라는 이름에 비밀번호(IDENTIFIED BY) '비밀번호'와 함께 유저를 생성(CREATE USER)한다.

    GRANT 권한 ON 데이터베이스.테이블 TO '아이디'@'호스트' WITH GRANT OPTION;
    => '데이터베이스'의 '테이블'을 대상으로 호스트에서 접속하는 '아이디'에 대해 권한(ALL, SELECT, INSERT, UPDATE, DELETE) 권한을 부여하며(GRANT) 부여받은 권한을 다른 사용자에게 부여할 수 있도록 허용한다(WITH GRANT OPTION).

    DROP DATABSE IF EXISTS 데이터베이스;
    => '데이터베이스'가 존재한다면(IF EXISTS) 해당 이름의 데이터베이스를 삭제한다(DROP DATABASE).

    CREATE DATABASE IF NOT EXISTS 데이터베이스;
    => '데이터베이스'가 존재하지 않는다면(IF NOT EXISTS) 데이터베이스를 생성한다(CREATE DATABASE).

    USE '데이터베이스';
    => '데이터베이스'를 사용한다.

    CREATE TABLE 테이블(속성 type(size) NOT NULL PRIMARY KEY, ...)
    => '테이블'을 생성한다(CREATE TABLE). type형의 크기가 size인 '속성'에 빈 값을 허용하지 않으며(NOT NULL) 해당 속성을
    기본키로 설정한다(PRIMARY KEY).

    INSERT INTO '테이블' VALUES('a1', ...)
    => '테이블'에 속성 값(VALUES) ['a1', ...]을 추가한다.

    SELECT [DISTINCT | ALL] '속성 리스트'(a1, a2, ...) OR 집계 함수
    FROM '테이블리스트'(t1, t2, ...)
    WHERE '조건식'
    GROUP BY '기준 속성 리스트'
    HAVING '그룹 조건식'
    ORDER BY {정렬 방법[ASC | DESC]}
    => '테이블 리스트'들에서 '속성 리스트'에 해당하는 속성들을 '조건식'에 맞게 필터링하고 반환
    집계 함수(SUM 등)를 요구할 경우 GROUP BY에서 '기준 속성 리스트'들로 묶어서 그룹화한 후 집계 함수가 각 그룹에 대한 연산을 마친 뒤에 HAVING의 조건식을 적용하여 반환
    ORDER BY를 통해 최종 테이블을 정렬

집합 연산자 : UNION, INTERSECT, EXCEPT, MINUS

서브 쿼리문 : where 절에 검색 조건을 실시간으로 만들어야 하는 경우 사용한다.

    SELECT '속성1'
    FROM '테이블1'
    WHERE '속성2' IN (값 리스트 혹은 쿼리문);
    => 테이블1에서 '속성2'가 값 리스트 중 하나의 값 또는 퀴리문을 만족하는 값을 갖는 튜플의 '속성1'의 값을 검색한다.

    SELECT '속성1'
    FROM '테이블1'
    WHERE [EXISTS | NOT EXISTS] (쿼리문);
    => 테이블1에서 쿼리문에 해당하는 값이 존재하는 튜플의 '속성1'의 값을 반환한다.

조인 검색

    크로스 조인 : 카티션 프로덕트
    
    SELECT [속성1, 속성2, ...] 
    FROM 테이블1, 테이블2(or FROM 테이블1 CROSS JOIN 테이블2);
    => 테이블1, 테이블2를 카티션 프로덕트한 테이블에서 속성1, 속성2, ...를 포함하는 튜플을 반환

    동등 조인 : = 연산자 사용

    SELECT [속성1, 속성2, ...]
    FROM 테이블1, 테이블2 WHERE 테이블1.속성1 = 테이블2.속성1
    (or FROM 테이블1 JOIN 테이블2 ON 테이블1.속성1=테이블2.속성1);
    => 테이블1과 테이블2에서 속성1의 속성 값이 같은 튜플들에서 속성1, 속성2,...를 가진 튜플들을 반환

    셀프 조인

    SELECT S1.이름, S2.이름
    FROM 학생 S1 JOIN 학생 S2 ON S1.주소 = S2.주소
    WHERE S1.학년 > S2.학년
    => 학생 테이블을 S1, S2로 나눠 주소가 같은(ON S1.주소 = S2.주소) 학생의 이름을 나열한다. 이 때 S1의 학년이 S2의 학년보다 높은 테이블만 뽑는다.

    외부 조인 : 조인 대상의 테이블의 모든 행들이 결과에 포함되기를 원할 때 사용

    SELECT 학생.학번, 학년, 이름
    WHERE 학생 LEFT OUTER JOIN 수강 ON 학생.학번 = 수강.학번
    => 과목 수강여부에 상관없이 모든 학생의 학번, 학년, 이름을 검색

삽입문

    INSERT INTO 테이블([속성 리스트])
    VALUES ([값 리스트]);
    => 테이블에서 [속성 리스트]에 해당하는 속성들에 [값 리스트]를 추가한다.

수정문

    UPDATE 테이블
    SET 속성 = 값 또는 산술식
    WHERE 조건식
    => 테이블에서 조건식에 해당하는 튜플의 속성 값을 수정한다.

삭제문

    DELETE FROM 테이블
    WHERE 조건식
    => 테이블에서 조건식에 해당하는 튜플을 삭제한다. 조건식이 없을 경우 모든 튜플을 제거하는데 되돌릴 수 없다.
    테이블을 제거하지는 않는다.

    DROP TABLE 테이블
    => 테이블 자체를 제거한다. 참조하고 있는 자식 테이블을 먼저 제거해야 한다.

테이블 수정 : 가급적 최소한으로 사용

    ALTER TABLE 테이블
    { [ADD|MODIFY] 속성 데이터유형 [NULL | NOT NULL] [DEFAULT 기본 값] }
    | { ADD CONSTRAINT 제약조건이름 제약조건상세내용 }
    | { DROP COLUMN 열이름 }
    | { DROP CONSTRAINT 제약조건이름 };
    => 테이블에 열과 제약조건을 추가하거나 제거한다.

권한 철회

    REVOKE 권한 ON 데이터베이스.테이블 FROM '사용자'@'호스트';
    => 호스트에 있는 사용자로부터 데이터베이스의 테이블의 권한을 철회한다.

접속 중인 계정 확인

    SHOW PROCESSLIST;


