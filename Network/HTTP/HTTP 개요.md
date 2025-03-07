HTTP(Hypertext Transfer Protocol) : 웹 브라우저와 웹 서버 간 데이터를 주고받기 위한 통신규약(프로토콜). 애플리케이션 계층의 프로토콜이다. 인터넷 전송 프로토콜로 TCP/IP를 사용한다. TCP/IP는 하드웨어적인 특성을 숨기고 어느 네트워크든 신뢰성있는 통신을 보장한다. 

웹 서버는 데이터를 저장하고 클라이언트는 사용자가 요청한 데이터를 제공한다.

웹 리소스의 종류 : 정적 파일, 동적 리소스(요청에 따라 콘텐츠 생산)

웹은 데이터 객체에 MIME 타입이라는 데이터 포멧 라벨을 붙임. 이를 통해 웹 브라우저는 다룰 수 있는 타입인지 확인할 수 있음.

사선(/)으로 구분되고 주 타입과 부 타입으로 이루어진 문자열 라벨(ex. text/html, text/plain 등)

URI(Uniform Resource Identifier) : 우편물 주소와 비슷하게 정보 리소스를 고유하게 식별하고 위치를 저장할 수 있음. 모든 형태의 식별자

URL(Uniform Resource Locator) : 리소스 식별자의 기본 형태. 리소스의 구체적 위치와 접근 방법으로 식별함.
(ex. http://www.hello.com/hi/hello.gif, http 프로토콜을 사용하고, www.hello.com으로 이동하여 hi/hello.gif라고 불리는 리소스를 가져와라)

URI가 URL을 포함하는 더 큰 개념임

트랜잭션 : 클라이언트와 서버 간의 하나의 request와 response로 이루어진 데이터 교환

    요청 메시지 구조
    <http 메서드> <경로> <http 버전>
    <헤더>

    <본문> (선택)

    http 메서드 : 클라언트가 서버에 수행하려는 작업(GET(read), POST(create), PUT(update), DELETE(delete) -> crud라고 불림)

    경로 : 리소스의 위치

    헤더 : 추가 정보(auth, 인증 토큰 등)

    본문 : 요청 데이터(post, put 등에서 사용)

    응답 메시지 구조
    <http 버전> <상태 코드> <상태 메시지>
    <헤더>

    <본문> (선택)

    상태 코드 : 요청 결과를 나타냄(200(성공), 404(리소스 없음), 500(서버 에러))

    상태 메세지 : 상태 코드 설명하는 텍스트(OK, NOT_FOUND 등)
    
    헤더 : 응답의 추가 정보(Content-Type, Content-Length)
    
    본문 : 요청된 리소스 데이터

웹페이지는 하나의 리소스가 아닌 여러 리소스의 모음이다.

HTTP 메시지는 단순 줄 단위의 텍스트 문자열

HTTP를 사용하여 TCP/IP통신을 하는 순서

    1. 웹 브라우저는 서버의 URL에서 호스트명 추출

    2. 웹 브라우저는 서버의 호스트명을 IP로 변환

    3. 웹 브라우저는 URL에서 포트번호 추출(기본 80번 포트)

    4. 웹 브라우저는 웹 서버와 TCP커넥션

    5. 웹 브라우저가 서버에 HTTP Request

    6. 서버는 웹 브라우저에 HTTP Response

    7. 커넥션이 닫히면 웹브라우저가 리소스를 보여줌

웹의 구성요소

    proxy : 클라어언트와 서버 사이 HTTP 중개자. 보안, 통합, 최적화를 위한 중요한 구성요소이다. 클라이언트의 모든 요청을 받아 서버에 전달함. 사용자를 대신해서 서버에 접근. 주로 보안을 위해서 사용되고 요청과 응답을 필터링함.

    cache : 많이 찾는 웹페이지를 클라이언트 가까에 보관하는 HTTP 창고. 웹 캐시와 캐시 프락시는 자신을 거쳐가는 리소스들 중 가장 자주 찾는 것을 사본으로 저장하는 서버이다. 클라이언트가 같은 문서를 요청하면 캐시가 가지고 있던 사본을 전달. 멀리 떨어진 웹보다 캐시 서버를 통해서 더 빠른 접근이 가능함. 캐시 서버의 컨텐츠를 최신 버전으로 유지하고 보안에도 신경쓴다.

    gateway : 다른 애플리케이션으로 연결된 웹 서버. HTTP 트래픽을 다른 프로토콜로 변환하기 위해 사용됨. 리소스를 가지고 있는 서버인 것처럼 요청을 다룸. 클라이언트는 알아챌 수 없음.

    tunnel : HTTP통신을 전달하기만 하는 proxy. raw데이터를 열지않고 그대로 전달해주는 애플리케이션. 비 http 데이터를 http 연결을 통해 그대로 전송하기 위해 사용됨.

    agent : 자동화된 HTTP요청을 만드는 semi-intelligent 웹 클라이언트. 사용자를 위해 http 요청을 만듦