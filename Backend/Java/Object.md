# Object

Java에서 최상위 부모 클래스

Java 내 모든 클래스는 Object를 직/간접적으로 상속한다.

즉, Object의 메소드들을 오버라이드 할 수 있음

    equals(Object o) : 두 객체가 논리적으로 같은지 비교함. 
    기본은 참조 비교(==)지만, 주로 내용 비교로 오버라이딩함

    hashCode(): 객체의 해시코드 반환. equals()를 오버라이드하면 같이 오버라이드해야함.

    HashMap, HashSet, HashTable에서 키 비교의 핵심
    
    toString(): 객체를 문자열로 표현. 디버깅, 로그에 사용
    
    clone(): 얕은 복사를 진행함. Cloneable 인터페이스를 구현해야 사용 가능.

    일반적으로 사용하지 않음. 깊은 복사를 위해 팩토리 메서드나 복사 생성자를 사용
    
    finalize(): 가비지 컬렉션 직전에 자원 정리에 사용함.
    거의 사용하지 않고, 대신 try-with-resources를 사용함
    
    getClass(): 객체의 클래스 정보를 반환함

Object 객체는 다형성을 기반으로 하며, 어떤 타입이든 Object로 받을 수 있음

즉, List<Object>같이 사용하면, 컬렉션에 타입이 다른 객체들을 한꺼번에 담을 수 있음