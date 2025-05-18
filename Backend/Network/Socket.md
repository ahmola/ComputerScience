# Socket

네트워크에서 통신하는 양쪽 프로세스간의 연결 인터페이스이다.

풀어서 설명하면, 서버와 클라이언트가 데이터를 주고받기 위한 통로라고 보면 된다.

소켓은 프로세스 간 통신을 위해 IP Address + Port Number로 만든 가상의 전화기로, 운영체제가 제공하는 네트워크 인터페이스이다.

TCP/IP 상에서 작동한다.

운영체제가 직접 네트워크를 다루기 힘들기 때문에 프로그래밍 레벨에서 네트워크를 다루는 수단이다.

소켓은 다음과 같이 구성된다.

    <프로토콜, IP 주소, 포트 번호>

## TCP Socket 통신 흐름(Server-Client 구조)

![img](https://media.geeksforgeeks.org/wp-content/uploads/20220330131350/StatediagramforserverandclientmodelofSocketdrawio2-448x660.png)

- 서버

        1.	socket() - 소켓 생성
        
        2.	bind() - IP, 포트 바인딩
        
        3.	listen() - 연결 요청 대기
        
        4.	accept() - 클라이언트 연결 수락
        
        5.	recv() - 데이터 수신
        
        6.	send() - 데이터 전송
        
        7.	close() - 소켓 종료

- 클라이언트

        1.	socket() - 소켓 생성
        
        2.	connect() - 서버에 연결 요청
        
        3.	send() - 데이터 전송
        
        4.	recv() - 데이터 수신
        
        5.	close() - 소켓 종료

## 예시(Python)

Server

    import socket

    // 소켓 생성
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    // IP, port 바인딩 -> 'localhost'의 '12345'번 포트에서 들어오는 연결 요청을 기다릴 준비를 마침
    server.bind(('localhost', 12345))
    // 요청 대기
    server.listen()

    // 클라이언트 연결 요청 수락
    conn, addr = server.accept()
    print('Connected by', addr)

    // 요청 데이터 수신
    data = conn.recv(1024)
    // 응답 데이터 송신
    conn.sendall(b'Hello, Client!')
    // 소켓 종료
    conn.close()

Client

    import socket

    // 소켓 통신
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    // 해당 서버에 연결 요청 -> localhost의 12345번 포트에 연결 요청
    client.connect(('localhost', 12345))

    // 요청 데이터 송신
    client.sendall(b'Hello, Server!')
    // 응답 데이터 수신
    data = client.recv(1024)
    print('Received:', data.decode())
    // 소켓 종료
    client.close()

소켓은 실시간 통신이 필요한 채팅이나 게임, 알림 등

지속적인 연결과 빠른 응답이 필요한 경우에 사용된다.

# WebSocket

웹 환경에서 클라이언트(브라우저)-서버 간 양방향 통신을 제공하는 인터페이스이다.

HTTP와 달리 연결되면 계속 유지되며 실시간 통신이 가능하다.

## 동작 과정

1. 핸드셰이크

    - 처음에는 HTTP로 연결 시작

    - 클라이언트가 HTTP 요청에 Upgrade: Websocket 헤더를 붙여 서버에 보냅니다.

    - 서버가 수락하면 HTTP를 WebSocket 프로토콜로 바꿈

    - 이후부터 TCP 상에서 WebSocket 프레임을 주고받는다.

2. 연결 유지

    - 한 번 연결되면 클라이언트와 서버는 지속적인 TCP 연결을 유지한다.

    - 별도 요청없이 서버는 클라이언트에게 메시지(프레임)를 보낼 수 있다.

    - 역으로, 클라이언트도 언제든 서버에게 메시지를 보낼 수 있다.

## 예제(Spring)

서버

    @Configuration
    @EnableWebSocket
    public class WebSocketConfig implements WebSocketConfigurer {
        private final MyWebSocketHandler handler;

        public WebSocketConfig(MyWebSocketHandler handler) {
            this.handler = handler;
        }

        @Override
        public void registerWebSocketHandlers(WebSocketHandlerRegistry registry) {
            registry.addHandler(handler, "/ws").setAllowedOrigins("*");
        }
    }

    @Component
    public class MyWebSocketHandler extends TextWebSocketHandler {

        @Override
        public void afterConnectionEstablished(WebSocketSession session) throws Exception {
            System.out.println("클라이언트 연결됨: " + session.getId());
            session.sendMessage(new TextMessage("서버에 연결되었습니다!"));
        }

        @Override
        protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
            System.out.println("받은 메시지: " + message.getPayload());
            // 받은 메시지를 그대로 다시 클라이언트로 보냄 (에코)
            session.sendMessage(new TextMessage("서버 응답: " + message.getPayload()));
        }

        @Override
        public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
            System.out.println("클라이언트 연결 종료: " + session.getId());
        }
    }

클라이언트

    @ClientEndpoint
    public class MyWebSocketClient {

        @OnOpen
        public void onOpen(Session session) {
            System.out.println("서버에 연결됨");
            try {
                session.getBasicRemote().sendText("안녕하세요 서버!");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        @OnMessage
        public void onMessage(String message) {
            System.out.println("서버로부터 받은 메시지: " + message);
        }

        @OnClose
        public void onClose(Session session, CloseReason reason) {
            System.out.println("서버와 연결 종료: " + reason.getReasonPhrase());
        }

        @OnError
        public void onError(Throwable throwable) {
            System.err.println("에러 발생: " + throwable.getMessage());
        }

        public static void main(String[] args) {
            WebSocketContainer container = ContainerProvider.getWebSocketContainer();
            String uri = "ws://localhost:8080/ws";
            try {
                container.connectToServer(MyWebSocketClient.class, URI.create(uri));
                Thread.sleep(5000); // 잠시 대기하여 메시지 수신 대기
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }