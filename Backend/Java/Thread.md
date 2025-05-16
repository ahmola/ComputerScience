# Thread

병렬 프로그래밍의 핵심으로, CPU 코어를 좀 더 효율적으로 사용하기 위해, I/O 대기 없이 여러 작업을 동시에 수행할 수 있게 해준다.

하나의 프로세스 내에서 실행되는 독립적인 실행 흐름(작업 단위)

프로세스에는 자원이 있고, 스레드는 그 자원을 공유하며 실행 흐름만이 독립적으로 진행됨

즉, 여러 스레드가 있다면 동시에 여러 작업이 가능함

메모리를 공유하고 통신이 빠르지만, 동기화에 주의해야함

## Java Thread의 원리

자바에서는 OS레벨의 스레드(네이티브 스레드)를 사용함

JVM이 내부 Thread Scheduler를 사용하여 스레드를 스케쥴링함

## Java에서의 Thread

    class MyThread extends Thread {
        @Override
        public void run() {
            System.out.println("스레드 실행");
        }
    }

    new MyThread().start();

run()은 작업을 정의하고, start()로 스레드를 시작함(run은 절대 직접 호출해서는 안됨)

실제로는

    class MyRunnable implements Runnable {
        @Override
        public void run() {
            System.out.println("Runnable 실행");
        }
    }

    Thread t = new Thread(new MyRunnable());
    t.start();

이런 방식이 많이 사용됨.

더 유연하고, 다중 상속 시에 문제가 없음

## Lifecycle

    NEW → RUNNABLE → RUNNING → (BLOCKED / WAITING / TIMED_WAITING) → TERMINATED

