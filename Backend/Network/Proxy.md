# Proxy 

클라이언트와 서버 사이에서 중계자 역할을 한다.

클라이언트는 프록시 서버를 통해 서버와 간접 통신을 하며,

클라이언트의 요청을 받아서 수정/캐싱/우회 등의 작업을 하여 서버에 대신 전달함

클라이언트는 내부 서버의 존재를 모르므로 보안+확장성+유연성을 확보할 수 있다.

## 목적

1. 보안 : 클라이언트 IP를 숨기고 서버 IP를 외부에 노출하지 않음. 방화벽 지원

2. 캐싱 : 정적 리소스 요청 등을 빠르게 응답

3. 접근 제어 : 특정 URL이나 도메인 차단(학교/회사에서 사용)

4. 로깅 및 모니터링 : 네트워크 활동 분석

5. 로드밸런싱 : 서버 부하를 분산시킴

6. TLS termination : HTTPS처리를 프록시에서 먼저 수행

클라이언트를 보호하기 위해서 사용하는 경우가 많고, 반대로 리버스 프록시의 경우에는 서버를 보호하기 위해서 사용한다.

만약 정방향 프록시만 있다면 -> 내부 사용자의 외부 접근은 컨트롤해도 외부에서 내부로 오는 요청은 필터링/로드밸런싱이 불가능 
-> 악용할 수 있음

반대로 리버스 프록시만 있다면 -> 외부 요청의 부하 분산 및 필터링은 가능하나 내부에서 외부의 위험한 리소스에 접근하거나 정보 유출 등 컨트롤 힘듦
-> 마찬가지로 악용 소지가 있음