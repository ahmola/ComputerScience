# Callable

Java에서 스레드 작업을 정의하는 인터페이스로, Runnable의 단점을 보완한 형태

리턴값을 가질 수 있고, exception throw가 가능함

    @FunctionalInterface
    public interface Callable<V> {
        V call() throws Exception;
    }

함수형 인터페이스로 call 단 하나의 메소드만을 가지며, 반환 타입 정의가 가능함. 람다식으로 표현가능

결과값이 필요한 작업에 쓰이며, 예외 처리가 가능하고, Thread Pool과 함께 비동기 처리가 필요할 때, 병렬 작업 후 결과를 일괄 처리할 때 사용하게 된다.

    List<Callable<Integer>> tasks = Arrays.asList(
        () -> 1,
        () -> 2,
        () -> 3
    );

    // 스레드 풀 생성
    ExecutorService executor = Executors.newFixedThreadPool(3);

    // 비동기적으로 스레드 결과값을 저장
    List<Future<Integer>> futures = executor.invokeAll(tasks);

    // 결과값 출력
    for (Future<Integer> f : futures) {
        System.out.println(f.get());  // 1, 2, 3
    }

