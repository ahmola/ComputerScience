# Executor

Java에서 스레드를 직접 만들고 관리하는 수고를 줄이기 위해 등장하는 스레드 실행 프레임워크

스레드를 만들고 관리하는 책임을 Executor 인터페이스가 대신한다.

기존 방식으로 스레드를 하나하나 직접 생성하면 비효율적이고 자원 낭비가 심함

    Runnable task = () -> System.out.println("Hello");
    Thread thread = new Thread(task);
    thread.start();

그래서 등장한게 Executor 프레임워크로, 인터페이스이다.

exeuctor() 메소드 하나만 정의되어 있다.

이를 기반으로 다양한 스레드 풀 기반 구현체가 존재한다.

## 주요 구현체

- ExecutorService : Executor를 상속하며 Future<T>로 결과를 비동기 반환

- ThreadPoolExecutor : 스레드 풀 기반 실행기. 실질적인 핵심 구현체

- ScheduledExecutorService : 정해진 시간마다 작업 실행 가능 (예약 실행)

## ExecutorService로 실행

    ExecutorService executor = Executors.newFixedThreadPool(2);

    executor.submit(() -> {
        System.out.println("작업 1 실행 중");
    });

    executor.submit(() -> {
        System.out.println("작업 2 실행 중");
    });

    executor.shutdown();  // 작업 제출은 중단하고, 기존 작업만 수행

- Executors.newFixedThreadPool(2) : 스레드 2개로 스레드 풀 구성
- submit() : 작업 큐에 등록하고 스레드 풀에서 처리
- shutdown() : 더 이상 작업을 받지 않고, 현재 작업만 마무리

## Future를 사용하여 작업 결과 받기

    ExecutorService executor = Executors.newSingleThreadExecutor();

    Future<Integer> future = executor.submit(() -> {
        Thread.sleep(1000);
        return 42;
    });

    System.out.println("결과: " + future.get());  // 42 출력
    executor.shutdown();

- Future<T> : 작업 결과를 비동기적으로 받게 해주는 객체
- .get() : 결과를 받을 때까지 블로킹

## 정리

대량의 병렬 작업 처리가 필요할 때, 스레드 수를 제한할 때, 주기적인 작업 예약이 필요할 때, 작업결과를 추적하거나 취소하고 싶을 때 사용한다.

반드시 shutdown()/shutdownNow()를 실행해야 JVM에서 종료가 됨

안하면 백그라운드에서 계속 살아서 자원 낭비


.submit() 외에도 Runnable에서 Callable 지원