# Java Virutal Machine

Java프로그램 실행을 위한 가상머신이다.

Java는 바이트코드로 소스코드가 변환되어 컴파일한 뒤에 JVM을 통해 실행이 된다.

JVM으로 어디서든 실행가능한 플랫폼 독립성이 제공된다(Write Once, Run Anywhere).

## JVM 구성요소

1. Class Loader
    - 실행 중에 필요한 클래스를 동적으로 로드한다.
    - 클래스의 경로를 관리하고 클래스를 메모리에 로드한다.
    - 부트스트랩, 애플리케이션, extension 클래스 로더가 존재한다.

2. Runtime 데이터 영역

    JVM은 런타임 환경에서 여러 메모리 영역을 관리한다.

    - 메소드 영역 : 클래스의 메타데이터 저장
    - Heap : 모든 객체가 할당되는 영역. 객체 생성과 소멸이 이루어짐
    - Stack : 메소드를 호출하면 메소드의 지역 변수와 호출된 메소드의 상태 저장
    - Program Counter Register : 실행 중인 메소드의 주소 추적 레지스터
    - Native Method Stack : Java외에 다른 네이티브 코드가 실행되는 Stack. C/C++로 구현됨

3. JIT Compiler(Just-In-Time Compiler)

    - JVM은 인터프리터 방식으로 바이트코드를 실행하는데, 효율을 높이기 위해 JIT컴파일러가 반복적으로 호출되는 코드들을 기계어로 변환한다.
    - 런타임 중에 바이트코드를 컴파일한다. 성능 개선을 위해 네이티브 머신 코드를 생성한다. 자주 사용되는 코드를 네이티브 코드(운영체제에 맞게 컴파일된 기계어)로 변환.

4. Garbage Collection
    
    - Heap에서 더 이상 사용되지 않는 객체를 자동 제거(메모리 누수 방지)
    - Mark-and-Sweep, Generational Garbage Collection 등 다양한 알고리즘 사용

## JVM 동작 과정

1. Java 소스코드(.java)가 컴파일되어 바이트코드(.class)로 바뀜

2. Class Loader가 바이트코드를 메모리에 로드

3. JIT컴파일러와 인터프리터를 사용하여 기계어로 변환하고 실행

4. GC로 메모리 관리

## JVM 특징

- JVM만 있다면 어디서든지 Java파일 실행 가능

- 격리된 환경에서 실행되므로 시스템 충돌 방지

- 멀티스레딩을 기본 지원하여 병렬 처리 가능

- GC덕분에 개발자가 일일이 메모리 할당 및 해제를 신경쓰지 않아도 됨