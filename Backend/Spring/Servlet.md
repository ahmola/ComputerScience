# Servlet

Java EE의 웹 기반 서버 프로그램 구성 요소

HTTP 요청을 받아 응답을 생성하는 서버사이드 컴포넌트이다.

## 동작 원리

    클라이언트 → HTTP 요청 → 웹 컨테이너 → Servlet → 응답 → 클라이언트

## 핵심 컴포넌트

- Servlet Container(ex. Tomcat) : Servlet을 관리하는 실행 환경. 요청을 받아서 Servlet을 실행하고, 응답을 돌려준다.

- HttpServletRequest/HttpServletResponse : 요청과 응답 객체. 클라이언트와 Servlet간 데이터 교환을 담당함

- Servlet Interface : javax.servlet.Servlet 인터페이스가 기본 인터페이스로 쓰이며, 주로 HttpServlet 클래스를 상속

## 생명주기

- init() : 시작 시 1회 호출, Servlet 초기화

- service() : 매 요청마다 호출, 요청을 처리함

- destroy() : 종료 시 1회 호출, 리소스 정리

        public class MyServlet extends HttpServlet {
            @Override
            public void init() throws ServletException {
                System.out.println("초기화");
            }

            @Override
            public void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
                resp.getWriter().write("Hello Servlet");
            }

            @Override
            public void destroy() {
                System.out.println("종료");
            }
        }

## Servlet의 한계

- 유지보수 어려움

- View와 분리가 어려워 HTML코드를 자바에 직접 써야함

# Spring MVC

이러한 servlet의 한계를 극복하기 위해 등장함

Servelt위에서 작동하는 고수준 웹 프레임워크

## 내부 구조

    [Client] → [DispatcherServlet] → [HandlerMapping]→ [Controller]
                                            ↓
                                     [HandlerAdapter]
                                            ↓
                                   [ViewResolver→View]

- DispatcherServlet : Spring MVC의 중앙 컨트롤러. HttpServlet하위 클래스로 Servlet으로 동작함. Spring의 내장 톰캣이 관리하며, 요청을 받아서 알맞은 컨트롤러에 전달하도록 HandlerMapping에 전달

- HandlerMapping : 알맞은 컨트롤러가 요청을 처리하도록 결정함

- Controller : 사용자 정의 클래스로, 요청을 어떻게 처리할지 정의함.(@Controller, @RestController 사용)

- HandlerAdapter : 컨트롤러를 실제로 실행

- ViewResolver/View/@ResponseBody : JSP 등의 실제 뷰나 파일로 변환

## 예시 흐름

    1. GET /members → 브라우저 요청
    
    2. DispatcherServlet (Spring MVC의 Servlet)으로 요청 전달됨
    
    3. HandlerMapping이 "/members" URL에 대응하는 컨트롤러 검색
    
    4. 해당 컨트롤러의 메서드 실행
    
    5. 리턴값이 "members.jsp"인 경우 → ViewResolver가 JSP 뷰로 변환
    
    6. 최종 HTML/JSON 응답 생성 후 브라우저에 전달
