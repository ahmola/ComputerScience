# Spring Actuator

Spring Boot 애플리케이션의 상태를 모니터링하고 관리할 수 있도록 도와주는 서브 프로젝트

헬스 체크, 메트릭 수집, 트래픽 분석, 환경 설정 등의 다양한 모니터링 기능을 REST API로 제공

가시성 확보와 안정적인 운영 제공에 필수적인 도구

## EndPoint

- /actuator/health : 헬스체크

- /actuator/info : 앱 빌드 정보/커스텀 정보 출력

- /actuator/metrics : JVM메모리, CPU사용량, HTTP 요청횟수 등 다양한 메트릭 수집

- /actuator/env : 앱 환경 변수 정보

- /actuator/beans : 등록된 스프링 빈 목록

- /actuator/loggers : 로그레벨 동적 조정

- /actuator/threaddump : 스레드 덤프 체크(장애 원인 분석에 사용)

## application.yml

    management:
        endpoints:
            web:
            exposure:
                include: "*"
        endpoint:
            health:
            show-details: always

## 고려사항

- Spring Security와 연계하여 인증 및 인가 설정

- 내부망 또는 관리자만 접근 가능하도록 방화벽 설정

- 필요한 엔드포인트만 선택적 노출

모니터링 시스템인 Grafana, Datadog, Prometheus 등과 연계하여 사용한다.