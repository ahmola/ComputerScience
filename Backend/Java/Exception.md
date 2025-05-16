# Exception

에러가 발생했을 때, 그 상황을 객체로 캡슐화한 것

예외가 발생하면 프로세스가 중단되고, 해당 예외를 처리하는 catch블록으로 이동함

예외 처리는 Java에서 무조건 강제된다.

    try {
        // 예외가 발생할 수 있는 코드
    } catch (ExceptionType e) {
        // 예외 처리 코드
    } finally {
        // 예외 발생 여부와 관계없이 실행 (자원 정리 등)
    }

예외에는 두 가지 Checked와 Unchecked가 존재한다.

Checked Exception은 Exception을 상속하고 반드시 try-catch-throw를 거치게 된다.

외부 환경 관련 문제로 발생하며(파일, DB 등), IOException이나 SQLException이 대표적인 예이다.

Unchecked Exception은 RuntimeException을 상속하며, 강제로 처리할지는 선택 사항이다.

보통은 디버깅을 위해서 사용되며, NullPointerException이나 ArithemticException 등이 대표적이다.

## throw와 throws

throw는 예외를 직접 발생시키고, throws는 예외를 호출자에게 넘김