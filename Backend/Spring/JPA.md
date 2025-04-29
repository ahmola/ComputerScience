우선 JPA를 알려면, ORM(Object-Relational-Mapping)에 대해서 알아야 한다.

# ORM
객체와 관계형 DB간 자동 매핑 기술

즉, 자바 클래스와 테이블을 자동 매핑해준다.

객체는 행(데이터), 클래스 필드는 열(속성)으로 정의된다.

SQL없이도 데이터에 접근할 수 있다.

전통적인 JDBC방식에선

    Connection con = DriverManager.getConnection(...);
    PreparedStatement ps = con.prepareStatement("SELECT * FROM user WHERE id = ?");
    ps.setLong(1, 1L);
    ResultSet rs = ps.executeQuery();
    User user = new User();
    user.setName(rs.getString("name"));
    // ...

이렇게 복잡한 설정을 통해서 DB에 접근해야 했다.

하지만 ORM(JPA)을 사용하면

    User user = entityManager.find(User.class, 1L);

이렇게 한 줄로 DB에 접근이 가능하다.

### 동작 방식

    1. Entity 클래스 정의 : DB테이블과 매핑되는 클래스위에 @Entity 어노테이션을 붙여서 정의한다

    2. Entity Manager / Session Factory 사용 : 객체 상태를 관리(CRUD)

    3. SQL 자동 생성 : ORM을 통해 SQL없이 DB와 통신

### 핵심 구성 요소(JPA)

    1. @Entity : 테이블과 매핑되는 클래스
    
    2. @Id : 기본 키 설정

    3. @Column : 속성 매핑

    4. @OneToMany/@ManyToOne : 다대일 관계 매핑
 
    5. EntityManager : ORM에서 객체의 CRUD기능을 맡는다.

# JPA (Java Persistance API)

자바 표준의 ORM Specification이다.

인터페이스 기반 API로, @Entity, EntityManager, @OneToMany 등을 정의

실제 동작은 이룰 구현한 Hibernate같은 구현체가 담당함


### Hibernate

하이버네이트는 JPA에서 가장 널리 사용되는 구현체로, JPA 규칙대로 작동하며, Spring Data JPA 모듈에서 사용하는 구현체이다

    @Repository
    public interface UserRepository extends JpaRepository<User, Long> {
        List<User> findByName(String name);
    }

기본적으로 @Lazy Loading으로 영속성 컨텍스트(1차 캐시)에 의해 관리되므로 생명주기와 트랜잭션 관리에 주의가 필요함

Lazy Loading은 Hibernate는 프록시 객체(대리 객체)를 생성하여 여기서만 접근하다가 실제로 DB에 접근해야 될 때에만 DB 쿼리를 발생시킨다. 이를 통해, 불필요한 DB연산을 줄여 성능을 향상시킨다.

트랜잭션(논리 작업 단위, 여러 작업으로 묶일 수 있으며, 내부 작업이 모두 성공해야만 성공한 거로 간주)이 닫히게되면 프록시가 초기화되지 않아 에러 발생.

트랜잭션 내에서만 데이터를 다뤄야함

    SessionFactory (싱글턴)
    └── Session (트랜잭션 단위)
         ├── 1차 캐시
         └── Lazy Loading 대상 관리
    └── 공유되는 2차 캐시

    Session : Hibernate 내에서 트랜잭션, 캐시, flush 등의 단위를 관리함. 
    1차 캐시를 제공하고, 엔티티 CRUD, DB와 실제 커넥션 처리를 담당한다.
    open -> persist -> flush -> commit -> close 의 생명주기를 갖는다.

    SessionFactory : Session을 생성하는 공장으로, 싱글톤 객체여서 앱 내 하나만 존재한다.
    DB 연결, 엔티티 클래스 매핑, 캐시 설정(2차포함), Session 생성 등을 담당한다.

    1차 캐시 : 트랜잭션 내의 캐시로 Session이나 EntityManager로 존재함. 
    같은 데이터를 여러 번 조회해도 실제로는 한 번의 DB 접근만 발생

    2차 캐시 : SessionFactory레벨에서 동작. 여러 세션에 공유되는 글로벌 캐시. 기본적으로 비활성화됨
    별도의 캐시 라이브러리(Redis 등)이 필요하며, 엔티티 단위로 설정한다.
    동기화 이슈로 캐시 무효화 전략이 필요함

복잡한 쿼리는 @Query를 통해 정의할 수 있음

# 마이크로서비스 아키텍쳐에서의 JPA

마이크로서비스는 의존도 최소화를 목적으로 각 기능에 따라 서비스로 분류되어 각자의 DB를 가지므로 전통적인 JPA의 @OneToMany를 쓰는데에 한계가 있다.

즉, 직접적인 Join이 불가능하다.

이에 대한 대안으로 Kafka와 OpenFeign등을 사용한다.

### Kafka

카프카는 비동기 메시지 기반 통신으로 완전한 비동기 통신을 지원하며, 느슨한 결합이 가능하다.

예를 들어, 주문이 완료되면 마일리지가 적립되는 시스템에서 사용된다면, 주문이 완료될 때 메시지를 보내고

    // OrderService
    kafkaTemplate.send("order.completed", orderId);

수신 측에서 메시지를 받으면 마일리지를 적립한다

    // UserService Listener
    @KafkaListener(topics = "order.completed")
    public void handleOrderCompleted(String orderId) {
        // 마일리지 적립
    }

### OpenFeign

오픈페인은 동기 기반 HTTP통신으로 서비스들끼리 데이터를 주고받는다.

한 서비스에서 유저 서비스로부터 유저의 정보를 받으려고 한다면

    @FeignClient(name = "user-service")
    public interface UserClient {
        @GetMapping("/users/{id}")
        UserDto getUser(@PathVariable Long id);
    }

이렇게 유저 서비스로부터 유저의 정보를 요청하여 할 수 있다.

HTTP 기반, 명시적 API 호출, 간단하다는 점이 있다.

즉, 마이크로서비스 아키텍쳐에서는 각 서비스마다 독립적인 ORM 구조를 가지므로 내부에서만 @OneToMany/@ManyToOne/@ManyToMany를 사용하게되고, 외부 서비스는 이러한 메시징 모듈을 사용하여 처리하게 된다.
