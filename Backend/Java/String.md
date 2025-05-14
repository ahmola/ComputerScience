# String

불변 문자열로, 한번 생성되면 값 변경 불가능

내부적으로는 char[]이지만 변경 불가능

HashMap, Key에서 안정성 확보

String pool에 의해 메모리 확보하여 재사용 가능

그러나 객체를 계속 생성하면 비효율적

# StringBuilder

가변 문자열이며 비동기 환경에서 사용된다.

내부의 char[]로 직접 조작이 가능함.

비동기로 단일 스레드 환경에서 매우 빠른 성능을 보여준다.

.append()같은 메소드를 사용하여 조작 가능하다.

로그 메시지나 파일 조작, 대량 문자열(Lob) 생성 등에 사용된다.

# StringBuffer

가변 문자열이며 동기화 환경에서 사용된다.

StringBuilder와 거의 동일하며 synchronized를 사용하여 동기화 지원

멀티스레드 환경에서 안전한 조작이 가능함

그러나, StringBuilder보다는 느림

# String Pool

Java에서 문자열의 메모리 효율을 위해 만들어진 특수 영역.

Heap의 한 부분으로, 동일한 문자열 리터럴을 재사용하는 저장소이다.

예를 들어 String s = "hello" 같이 리터럴로 선언된 문자열이 String Pool에 저장되고 같은 문자열이 또 나오면 새로 만들지 않고 기존에 만들어 둔 문자열을 재사용

    String a = "hello";
    String b = "hello";
    System.out.println(a == b);  // true

실제로 메모리 주소를 비교해보면 두 값이 같다고 나옴.

즉, String Pool에서 똑같은 문자열을 같이 사용하는 중임.

그러나, new String으로 초기화하면 new는 무조건 새 객체를 Heap에 할당하므로 다른 객체가 됨

그렇기 때문에 String은 근본적으로 불변 객체일 수 밖에 없는데,

만약 가변 객체라면 위에 예에서 a의 문자열을 변경하게되면, b도 같이 바뀌게 되므로 설계 자체가 불변 객체로 설계됨

new String을 해도 .intern()을 사용하면 String Pool에 넣을 수 있다.

    String c = new String("hello").intern();
    System.out.println(a == c); // true

문자열이 자주 사용되는 자바에서는 메모리 효율성을 크게 올려줌