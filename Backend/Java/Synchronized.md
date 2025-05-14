# Synchronized

멀티스레드 환경에서 동기화를 보장하기 위해 사용되는 키워드

여러 스레드가 동시에 공유된 자원에 접근할 때, 데이터의 일관성과 정합성을 보장하는 행위이다.

JVM 내에 Montior Lock를 사용하여 객체 당 하나의 락이 주어지며, 스레드는 락을 휙득해야하만 해당 블록이나 메소드를 사용할 수 있음.

여러 스레드가 동시에 접근하는 경쟁 상태를 막기 위해(Race Condition)

1. 메소드 전체에 synchronized를 사용하는 인스턴스 락을 사용한다.

    public synchronized void myFunction() {
        // function work
    }

이렇게 설정하면, 객체 내에서 한 번에 하나의 스레드만 접근이 가능하다.

2. 임계 영역에만 지정하는 방법도 있다.

    public void myFunction(){
        synchronized (this){
            // fucntion work
        }
    }

더 정밀한 제어가 가능하며, 공통 자원 접근하는 부분에 대해서만 동기화를 하도록 할 수 있다.

3. 클래스 전체에 락을 걸 수 있다. static 메소드나 클래스 락 두 가지가 존재한다.

    public static synchronized void myFunction() {
        // 정적 자원 처리
    }

    synchronized (MyClass.class) {
        // 클래스 단위의 동기화
    }

가장 기본적이고 안정적이지만, 단순하기에 고성능 병렬 처리에는 한계가 있음.

복잡한 동기화에는 Lock, Concurrent 패키지 등이 필요함

# Volatile

Java 메모리 모델에서 가시성(Visibility)를 보장할 때 사용함

즉, 읽기 작업이 주 작업이고 쓰기 작업이 거의 없는 경우에 사용함

메인 메모리와의 동기화를 보장하며 여러 스레드가 접근해서 최신 정보를 얻을 수 있음

최신 값에 대한 즉각적인 확인이 스레드 간에 필요하고 연산이 원자성을 보장할 필요가 없는 경우에 사용된다.

락이 없어 누구나 최신 값에 접근할 수 있어 빠른 성능을 보장함.

Synchronized는 화장실 키라면, Volatile은 공용 게시판이라고 생각하면 된다.