# Runnable

Java에서 스레드로 실행될 작업을 정의하는 인터페이스

말 그대로 "작업"이며, 어떤 작업을 수행할 지 지정할 때 사용됨

    @FunctionalInterface
    public interface Runnable {
        public abstact void run();
    }

함수형인터페이스로 하나의 추상 메소드 run()만을 가지며, 매개변수와 리턴값이 존재하지 않음

람다식으로 표현 가능

    public class MyRunnable implements Runnable {
        public void run() {
            // work
        }
    }
    Runnable task = () -> {
        // lambda work
    };

    public class Main {
        public static void main(String[] args) {
            Thread thread1 = new Thread(new MyRunnable());
            Thread thread2 = new Thread(task);
            thread1.start();
            thread2.start();
        }
    }

스레드를 생성할 때, Runnable을 상속하여 정의한 작업(MyRunnable)을 매개변수로 받아서 thread를 실행한다.

start()를 하면 run()을 실행함

## Runnable과 Thread의 관계

Runnable은 작업 정의, Thread는 실행 주체이다.

Thread는 Runnable을 구현한 구현체를 인자로 받아서 내부 메소드 run()을 실행

## 단점

- 리턴값이 없어서 작업이 완료되었는지 여부를 알 수 없다.

- 예외를 throw하지 못함