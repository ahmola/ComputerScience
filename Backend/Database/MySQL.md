# MySQL

Oracle 사에서 제공하는 오픈소스 RDBMS

SQL 표준을 준수하며 ACID 트랜잭션, 고성능 READ/WRITE를 제공

LAMP(Linux/Apache/MySQL/Python)의 핵심

## 구조

1. Connection Layer
     - 사용자 인증, SSL처리, 커넥션 핸들링
     - 각 커넥션은 독립 스레드

2. SQL Layer
    - SQL Query 파싱 -> 구문 분석 -> 최적화 -> 실행 계획 수립
    - View, Stored Procedure 등 구현
    - Optimizer가 실행 계획 결정

3. Stored Engine Layer
    - 실제 데이터 CRUD
    - 여러 스토리지 엔진 플러그인 방식 지원

## InnoDB 스토리지 엔진

스토리지 엔진으로, MySQL에서 데이터를 실제 CRUD하는 핵심 컴포턴트

- ACID 트랜잭션 지원

- Mulit-Version Concurrency Control : 동시성 향상 기법, 락없이 SELEC로 데이터 읽기 가능

- B-Tree 인덱스 : 클러스터 인덱스를 사용하여 Primary Key 기준으로 실제 데이터 정렬 저장하고 보조인덱스로 Leaf Node에 Primary Key를 포함한다.

- Page와 Buffer Pool : 데이터를 16KB 페이지 단위로 관리,자주 접근하는 페이지는 메모리의 Buffer Pool에 캐시하고 LRU 알고리즘으로 교체

## SQL 처리 흐름

1. 클라이언트가 SQL 쿼리 전송

2. Parser가 SQL 문법 분석

3. Optimizer가 실행 계획 수립(비용 기반)

4. Executor가 실행 계획을 실행함

5. Storage Engine(Inno DB)가 실제 데이터 CRUD
