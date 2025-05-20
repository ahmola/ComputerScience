# Spring MVC

Servlet 기반 웹 애플리케이션 개발 Spring 웹 모듈

HTTP 요청을 처리하고, 응답을 생성하는 MVC구조를 효율적으로 구현할 수 있게 해주는 프레임워크이다.

## 구성요소

- Model : 데이터 및 비즈니스 로직

- View : 사용자에게 보여주는 화면/자료

- Controller : 요청을 받고 Model에 대한 작업 후 View로 전달

## 아키텍쳐

    1. 클라이언트 : /hello 요청
    
    2. DispatcherServlet : 요청 수신
    
    3. HandlerMapping : "/hello" → HelloController의 메서드 매핑 검색
    
    4. HandlerAdapter : 해당 메서드 실행
    
    5. Controller : 비즈니스 로직 수행, Model 객체 채우기
    
    6. DispatcherServlet : ModelAndView 반환 받음
    
    7. ViewResolver : 논리 뷰 이름 → 실제 JSP 파일 등으로 변환
    
    8. View : 렌더링 후 HTML 생성
    
    9. DispatcherServlet : 응답 반환

- DispatcherServlet : Spring MVC의 핵심 Servlet. 모든 요청의 진입점

- HandlerMapping : URL에 맞는 Controller 메서드를 찾아주는 컴포넌트

- HandlerAdapter : 찾은 Handler(Controller)를 실제로 호출

- Controller : 요청을 처리하는 사용자 정의 클래스(@Controller, @RestController)

- Model : 데이터를 담는 객체. Model, ModelMap, ModelAndView 등

- ViewResolver : 논리 뷰 이름  → 실제 View로 변환 (/WEB-INF/views/xxx.jsp 등)

- View : JSP, Thymeleaf, JSON 등 클라이언트에게 최종 전달할 화면
