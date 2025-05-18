# HyperText Transfer Protocol

웹에서 클라이언트와 서버 사이 통신을 정의하는 애플리케이션 레벨의 규약

기본 포트 : 80(HTTPS는 443)

기반 프로토콜 : TCP

MIME 타입 기반 프로토콜 전송

텍스트 기반 프로토콜

기본적으로 (클라이언트가 요청 -> 서버가 응답) 하는 방식이다.

## HTTP Methods

- GET : 리소스 조회, 캐시, 브라우저 북마크 등

- POST : 리소스 생성, 폼 제출, 로그인 등

- PUT : 리소스 전체 수정, 멱등성(같은 요청에 같은 응답) 보장

- PATCH : 리소스 일부 수정, 멱등성 보장하지 않음

- DELETE : 리소스 삭제, 멱등성 있음

- HEAD : 응답 body없이 헤더만 요청, 주로 상태 확인 용도

- OPTIONS : 허용된 메서드 확인, 사전 요청에 사용

## HTTPS Status Code

- 100번대 : 정보, 처리 중을 의미함, 거의 사용하지 않음

- 200번대 : 성공, 200 OK, 201 Created 등

- 300번대 : 리다이렉션, 301 Moved Permanently, 302 Found

- 400번대 : 클라이언트 오류, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found 등 클라이언트에 의해 발생한 오류를 나타냄

- 500번대 : 서버 오류, 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable 등 서버에서 발생한 오류를 나타냄

## 버전

- HTTP/1.0 : 연결 재사용 안됨, 매 요청마다 TCP 연결

- HTTP/2.0 : Keep-Alive로 연결 재사용, 헤더 기반 요청/응답 파이프라이닝

- HTTP/2 : 멀티플렉싱, 헤더 압축, 서버 푸시, 성능 대폭 향상

- HTTP/3 : UDP 기반 QUIC, 지연시간 줄이고 TLS 1.3 내장

## Stateless

Http는 무상태를 유지한다.

그 어떠한 상태도 유지하지 않는데,

그렇기 때문에 사용자 정보나, 누구와 통신했는지 등을 기록하지 않는다.

이는 세션/쿠키/토큰같은 통신 및 서비스에 필요한 정보 저장을 요구한다.

## HTTPS

정보 탈취 가능성이 있는 평문인 HTTP를 TLS를 사용하여 암호화된 통신을 제공한 통신이다.

인증서 기반 공개키 교환으로 기밀성+무결성+인증을 제공한다.

## 최적화

- HTTP 캐시 : Cache-Control

- 압축 : Content-Encoding

- CDN : 지리적으로 가까운 서버에서 리소스 제공

- 멀티플렉싱 : 하나의 연결로 여러 요청 병렬 처리

- 프리로드/프리패치 : 리소스 미리 요청

