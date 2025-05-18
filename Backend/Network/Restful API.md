# API

Application Programming Interface의 약자로, 프로그램과 프로그램 사이의 명세, 소통 수단을 의미한다.

API는 프로그램의 기능을 다른 프로그램이 사용할 수 있도록 한다.

요청을 보내면 해당 프로그램이 요청에 맞춰서 대신 실행해주고 결과를 반환해준다.

인터페이스이기에 내부 구현을 몰라도 사용할 수 있고,

요구하는 방식대로 요청을 보내면 해당 작업 서비스를 제공받을 수 있다.

즉, 원격으로 함수를 호출하는 방법으로

정해진 방식으로 요청하는 것을 API 호출이라고 한다.

정해진 Endpoint에 정해진 Method를 요청(Body, Header, Query)을 보내면, 알맞은 작업을 수행하여 응답한다.

# REST

REpresentational State Transfer의 약자로,

웹 기반 시스템 설계 원칙이다.

자원을 URI화하여 HTTP 메소드를 통해 자원을 조작함

## REST의 조건

- 클라이언트-서버 구조 : 사용자와 데이터 작업을 분리

- Stateless : 요청에 모든 정보를 포함하여 세션을 두지 않는다.

- Cachable : 응답에 캐시 여부 명시

- Layer 시스템 : 중간 게이트웨이와 프록시 사용

- 일관된 인터페이스 : URI + HTTP 규약을 따름

- Code on Demand : 클라이언트로 전송 가능함. 선택 사항이다. 

# RESTful API

이러한 REST의 조건을 잘 지킨 API를 RESTful API라고 한다.

즉, RESTful은 표준화된 방식으로 자원을 명확하게 조작하는 API라는 뜻이다.

## 특징

- 자원 중심 : URI는 "What"을 나타냄(/user/{user_id}/post/{post_id})

- 행위는 HTTP Method로 표현 : GET -> 조회, POST -> 생성, PUT -> 전체 수정, PATCH -> 일부 수정, DELETE -> 삭제

- Stateless : 모든 요청은 저장되지 않고, 서로 영향을 받지 않는 독립적인 상태여야 한다.

- 일관된 URI와 응답 구조 : 리소스 명명은 복수형으로 정의한다
ex) /users, /posts 등

RESTful 예

    POST /users
    Body: { "id": 1, "name": "hong" }

그러나, 현실적인 측면을 고려하여 REST를 완벽하게 따를 필요는 없다.



