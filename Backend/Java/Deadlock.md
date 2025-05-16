# Deadlock

자바 멀티스레드 프로그래밍 시에 발생할 수 있는 병목 현상

서로 자원을 점유하고 있어서 아무도 진행할 수 없는 상태를 말한다.

즉, 두 개 이상의 스레드가 서로 상대방의 자원을 기다리느라 영원히 멈춘 상태를 말한다.

멀티스레드가 자원을 잘못 잠궈서 서로를 영원히 기다리게 해서 발생하는 문제

    class A {
        synchronized void methodA(B b) {
            System.out.println("Thread1: methodA 시작");
            try { Thread.sleep(100); } catch (Exception e) {}
            b.last();  // B의 메서드에 접근 시도
        }

        synchronized void last() {
            System.out.println("A.last() 호출됨");
        }
    }

    class B {
        synchronized void methodB(A a) {
            System.out.println("Thread2: methodB 시작");
            try { Thread.sleep(100); } catch (Exception e) {}
            a.last();  // A의 메서드에 접근 시도
        }

        synchronized void last() {
            System.out.println("B.last() 호출됨");
        }
    }

    public class DeadlockDemo {
        public static void main(String[] args) {
            A a = new A();
            B b = new B();

            // 두 개의 스레드가 서로의 락을 기다리는 구조
            new Thread(() -> a.methodA(b)).start();  // Thread1
            new Thread(() -> b.methodB(a)).start();  // Thread2
        }
    }

## 발생 조건

- 상호 배제 : 자원은 한 번에 하나의 프로세스만 사용가능할 때

- 점유와 대기 : 자원을 점유한 상태에서 다른 자원을 기다림

- 비선점 : 다른 스레드의 락을 강제로 뺏을 수 없음

- 순환 대기 : 스레드들이 원형으로 자원을 기다림

이 네 가지가 모두 충족되면 데드락 발생

즉, 넷 중 하나만 사라져도 데드락이 발생하지 않음

## 해결방법

1. 락의 휙득 순서를 정한다.

2. tryLock()을 사용한다.

    if (lock1.tryLock(100, TimeUnit.MILLISECONDS)) {
        try {
            if (lock2.tryLock(100, TimeUnit.MILLISECONDS)) {
                try {
                    // critical section
                } finally {
                    lock2.unlock();
                }
            }
        } finally {
            lock1.unlock();
        }
    }

3. 타임아웃 + 감시 스레드 : 락 휙득 시간에 제한을 두고, 오래 대기하면 강제 중단하도록 한다.