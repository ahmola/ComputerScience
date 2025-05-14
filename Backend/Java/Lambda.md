# Lambda Expression(익명 함수)

    (매개변수들) -> {실행할 코드}

람다는 함수형 인터페이스를 구현한 것이다.

함수형 인터페이스는 단 하나의 추상 메소드만을 가진 인터페이스를 말한다.

@FunctionalInterface 어노테이션을 붙혀서 선언하며 단 하나의 메소드만을 가진다.

즉, 람다는 추상 메소드를 구현한 구현체이다.

    @FunctionalInterface
    interface MathOperation {
        int operation(int a, int b);
    }

    // 람다로 구현
    MathOperation add = (a, b) -> a + b;

## 메소드 참조

람다 표현식을 더욱 간결하게 표현하는 방법

메소드를 간접적으로 참조한다

    names.forEach(name -> System.out.println(name));

    // 메소드 참조로 변환
    names.forEach(System.out::println);

static 메소드도 참조가 가능하다