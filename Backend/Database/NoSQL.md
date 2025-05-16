# NoSQL

Not Only SQL의 약자로 RDBMS의 한계를 극복하기 위한 비관계형 데이터베이스 시스템이다.

유연한 스키마, 수평 확장성, 다양한 데이터 모델을 제공한다.

기존 RDBMS는 고정 스키마, 조인으로 인한 성능 저하, 수평 확장성 부족, 대량 비정형 데이터 처리의 비효율성 등의 한계가 존재했음

웹 2.0과 빅데이터, 모바일 시대가 도래하며 데이터 볼륨이 증가하고 고가용성, 빠른 응답, 분산 처리 등이 필요해짐

이러한 한계를 극복하고자 NoSQL이 탄생

NoSQL은 내부 구조와 데이터 모델에 따라 크게 4가지로 분류된다.

- Document : JSON/BSON 구조로 저장. 대표적으로 MongoDB

- Key-Value : Key-Value 쌍으로 저장. Redis가 대표적

- Column-Family : 열 중심으로 저장하며 대용량 분산 처리에 사용된다. Cassandra가 대표적이다.

- Graph : 노드-간선의 관계 중심 모델. Neo4j가 대표적

## CAP 이론

- Consistency : 모든 곳에서 동일한 데이터를 봄

- Availability : 모든 요청에 응답 보장

- Partition Tolerance : 네트워크가 끊겨도 시스템이 동작

Consistency, Availability, Partition Tolerance 이 세 가지를 동시에 만족시킬 수 없다는 이론

그래서 대부분, CP 또는 AP 중 하나를 선택하게 된다.

MongoDB가 대표적인 CP, Cassandra가 대표적인 AP 지향이다.

## BASE

RDBMS는 ACID를, NoSQL은 BASE 원칙을 따름

- Basically Available : 항상 응답(정확할 필요 없음)

- Soft state : 일시적인 변경이 있을 수 있음

- Eventually consistent : 일정 시간 후에 일관성 확보

정리하면 일관성보다는 가용성과 확정성에 초점을 둔다는 뜻이다.

### 장점

- 스키마리스 : 스키마가 없는, 그러니까 데이터 구조가 정해지지 않아서 비교적 유연한 구조를 가진다.

- 수평 확장성 : 샤딩, 레플리카를 쉽게 구성할 수 있다.

- 빅데이터 친화적 : 고속 쓰기/읽기 가능

- 특정 목적에 따라 최적화 : 그래프 탐색, TTL 캐싱 등

### 단점

- 조인 부재 : Application Layer, 즉 프로세스에서 데이터 통합이 필요함

- 트랜잭션 부재 : ACID가 아닌 BASE 적용

- 데이터 중복 허용 : 정규화보다는 성능 위주의 설계

- 고급 최적화 부재 : 퀴리 최적화가 미약하다

이러한 이유로, 실제로는 RDBMS와 NoSQL을 섞어서 사용한다.