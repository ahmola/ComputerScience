# springboot

전통적인 spring framkework의 복잡함을 줄이고, 빠르고 쉬운 애플리케이션 개발을 위해 설계된 Spring Framework의 확장

불필요한 코드를 줄이고 설정을 자동화하는데 중점을 둔 프레임워크

    스프링 프레임워크가 모든 도구가 구비된 창고라면, 스프링 부트는 특정 작업에 필요한 도구만을 담은 작은 도구 상자라고 볼 수 있다.

규칙기반설정(Convention over Configuration)은 미리 정의된 규칙과 표준을 사용하는 소프트웨어 디자인 패러다임으로 스프링부트는 이러한 디자인 패러다임을 채택하였다. 개발자들이 비즈니스 로직에 집중할 수 있도록 기본 규칙을 설정하였는데, 클래스의 이름이 데이터 테이블의 이름을 자동 매핑된다거나, 미리 설정된 라우팅 규칙들이 그 예이다.

스프링의 핵심 개념인 IoC와 DI는 객체 생성/관리 방식을 다룬다.

    DI(Dependency Injection, 의존성 주입) : 객체가 다른 객체를 의존(ex. a = new b(), a와 b는 서로 다른 클래스(또는 인터페이스), a는 b가 없다면 제대로 작동하지 않을 수 있는 관계)할 때, 이를 직접하는 것(new를 통한 초기화)가 아니라 외부에서 하는 것을 말한다. 즉 직접 생성하지 않고 의존 관계라는 사실만 알린다.

    IoC(Inversion of Control, 제어의 역전): 객체 생성과 의존성 주입을 개발자가 아닌 프레임워크가 담당한다. 기존에 new 키워드를 통해 직접 초기화하는 방식이 아니라 단순 객체 주입을 통해, 의존성을 SpringContext가 담당하게 된다.

이를 통해 결합도를 낮추고, 유지보수성이 낮아지고, 테스트가 쉬워진다.

이러한 의존성의 역전으로 만들어진 객체를 bean이라고 하며 Spring 컨테이너(Application Context)가 생성하고 관리한다.

기본적인 Spring IoC Container로는 BeanFacotry가 있고 이것이 최상단 컨테이너 인터페이스로 있다. 이를 확장하여 부가기능이 포함된 IoC컨테이너가 ApplicationContext이다.

Spring은 Bean을 생성하고 필요한 의존성을 주입한 뒤, 초기화 메서드를 호출하고, 애플리케이션 종료 시 소멸 메서드를 호출한다.

내부적으로 여러 모듈로 나뉘고, autoconfiguration과 embeded server를 중심으로 동작

# springboot의 간단한 구조

    Client(Web/API) - Controller - Service - Repository - Database

# springboot의 구성요소

    1. starter dependencies
        - 각 기능별 미리 정의된 starter 제공(ex. web, jpa, security)
    2. auto configuration
        - @SpringBootApplication을 통해 자동 설정 활성화
        - ClassPath에 있는 라이브러리를 보고 자동 설정(웹은 Tomcat을, JPA는 EntityManager를 구성)
        - application.yml(또는 properties를 통해 세부 설정 가능)
    3. embeded server
        - tomcat, jetty, undertow같은 웹 서버가 내장됨
        - 서버를 따로 설치할 필요없이 jar파일 실행 시 웹 서버 로드

모든 SpringBoot 애플리케이션은 @SpringBootApplication 어노테이션이 달린 main함수에서 시작함

    @SpringBootApplication
    public class MyApplication {
        public static void main(String[] args) {
            SpringApplication.run(MyApplication.class, args);
        }
    }
이렇게 내장 웹 서버를 시작한다.

application.yml(또는 properties)

    server:
    port: 8080

    spring:
    datasource:
        url: jdbc:mysql://localhost:3306/mydb
        username: root
        password: secret
기본적으로 스프링부트는 기본 HTTP 포트인 8080번 포트를 사용한다.

# 계층 구조

    1. Controller
        - 외부 요청(Request)를 받는 진입점
        - Rest API, 웹 요청을 받습니다.
        - 보통 @RestController로 선언

    2. Service
        - 비즈니스 로직 담당
        - 트랜잭션 관리, 도메인 처리 등
        - @Service로 선언
    
    3. Repository
        - 데이터베이스와의 연결
        - JpaRepository, CrudRepository인터페이스를 상속하여 DB 작업 자동화
        - @Repository 선언
    
    4. Domain/Entity
        - DB 테이블과 매핑되는 클래스
        - @Entity, @Table로 매핑

# 스프링부트의 내부동작 흐름

    1. 애플리케이션 실행
        - @SpringBootApplication이 붙은 클래스 실행 -> SpringApplicaiton.run() 실행
        - SpringContext 생성 : Bean객체관리, dependencies 주입
        - 내장 Tomcat 부팅
        - Bean 스캔 -> @Component, @Controller, @Service, @Repository 등을 등록

    2. 내장 톰캣(Web Server) 시작
        - 실행되면 HTTP요청을 수신 대기상태로 둔다.
        - DispatcherServlet(MVC 중심 컴포넌트, 요청 분배)을 Servlet으로 둔다. 서블릿은 간단하게 HTTP요청을 처리하는 프로그램이라고 생각하면 된다. 톰캣은 이러한 서블릿을 실행할 환경을 제공하고 관리한다. 즉, 서블릿에는 기능(비즈니스 로직)이 있고, 톰캣은 이를 관리/실행하는 서버의 역할을 한다. DispatcherServlet은 스프링의 요청을 처리하는 중앙 장치이다. 스프링 부트에서는 내장 톰캣이 디스패쳐서블릿을 관리하게 된다. 디스패쳐서블릿이 모든 요청을 받고 알맞은 컨트롤러 메서드를 실행한다. Controller 내의 함수들이 서블릿처럼 동작한다.
        - DispatcherServlet은 HTTP 요청을 받아 적절한 컨트롤러에 전달하고, 응답을 받아 클라이언트에 반환하는 역할을 한다.
    
    3. 요청 수신
        - HTTP 요청(Request)을 보내면 내장 톰캣이 수신
        - 톰캣이 요청을 DispatcherServlet으로 전달

    4. Spring MVC 처리 시작
        - DispatcherServlet이 HandlerMapping으로 컨트롤러에 매핑
        - HandlerAdapter로 실제 컨트롤러 호출
        - 호출된 컨트롤러가 서비스를 호출
    
    5. 비즈니스 로직 처리
        - @Service가 붙은 클래스인 서비스를 호출
        - 서비스는 다시 @Repository가 붙은 인터페이스인 레포지토리 호출
        - 레포지토리가 JPA를 통해 DB 계층에 접근하여 데이터를 CRUD 작업하여 서비스에 반환
        - 서비스는 컨트롤러로 비즈니스 로직의 결과를 컨트롤러로 반환
    
    6. 응답 반환(REST API)
        - 컨트롤러가 결과를 반환
        - DispatcherServlet이 JSON/HTML 여부를 판단
        - HttpMessageConverter를 사용하여 JSON반환
    
    7. 톰캣이 응답 전송
        - DispatcherServlet이 톰캣에 응답을 전달
        - 톰캣이 클라이언트로 응답 전송