# Thread Pool

일정 수의 스레드를 미리 생성해두고, 작업이 들어오면 생성된 스레드들을 재사용하는 구조

스레드를 직접 생성할 경우 비용이 크고, 너무 많이 만들게 되면 성능 저하가 발생하며 유지보수가 힘들기 때문에, 

Thread Pool로 미리 스레드를 생성해두고 재사용하여 효율적인 처리가 가능함

Java에서는 ExecutorService 인터페이스를 통해 Thread Pool을 제공하며, 팩토리 메소드로 Executors가 있다.

## 주요 매개변수
    corePoolSize : 기본적으로 유지할 스레드 수

    maximumPoolSize : 최대 스레드 수 (큐가 가득 찼을 때 확장 가능)
    
    keepAliveTime : 유휴 스레드의 생존 시간 (core 초과 분)
    
    workQueue : 작업을 담는 큐 (LinkedBlockingQueue 등)
    
    threadFactory : 스레드 생성 방법 지정
    
    rejectedExecutionHandler : 큐도 스레드도 꽉 찼을 때 처리 전략

    ExecutorService executor = new ThreadPoolExecutor(
        2, 4, 60, TimeUnit.SECONDS,
        new LinkedBlockingQueue<>(100)
    );

## 동작 순서

	1.	작업 제출 (submit() 또는 execute())

	2.	현재 스레드 수가 corePoolSize보다 작으면 새 스레드 생성
	
    3.	corePoolSize를 넘으면 workQueue에 작업을 저장
	
    4.	큐가 꽉 차면 maximumPoolSize까지 스레드 확장
	
    5.	그래도 부족하면 rejectedExecutionHandler 발동

## RejectedExecutionHandler

스레드도 꽉 차고, 큐도 꽉차서 더 이상 스레드를 추가할 수 없을 때 사용됨

- AbortPolicy(기본) : 예외를 발생시킴

- CallerRunsPolicy : 요청한 스레드에서 직접 실행

- DiscardPolicy : 폐기해버림

- DiscardOldestPolicy : 가장 오래된 큐 작업을 버리고 새 작업 추가