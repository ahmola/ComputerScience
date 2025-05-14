# Collection

데이터를 저장하고 조직하기 위한 자료구조 집합

List, Set, Queue 등이 존재(Map은 별개의 인터페이스)

## List

순서를 고려하고, 중복을 허용함

1. ArrayList : 배열 기반, 읽기 빠름, 삽입/삭제 느림

2. LinkedList : 연결 리스트 기반, 삽입/삭제 빠름, 접근 느림

3. Vector : ArrayList와 유사하나 동기화됨(구식)

4. Stack : Vector기반 후입선출 자료구조

## Set

중복 허용하지 않고, 순서 보장 여부는 구현체마다 다름

1. HashSet : 순서 없음, 중복 제거

2. LinkedHashSet : 입력 순서 유지

3. TreeSet : 정렬 순서 유지 (이진 탐색 트리 기반, Comparable 필요)

## Queue/Deque

선입선출의 구조

1. LinkedList : Queue, Deque 둘 다 구현

2. PriorityQueue : 우선순위 기반 정렬

3. ArraryDeque : 빠르고 효율적인 양방향 큐

## Map<Key, Value> 

키-값 쌍 저장, 키 중복 불가

1. HashMap : 순서없음, 널값 허용

2. LinkedHashMap : 입력 순서 유지

3. TreeMap : 키 정렬 (Comparable 필요)

4. HashTable : 구식, 동기화된 HashMap

### 주요 메소드

- add(E) : 요소 추가

- remove(Object) : 요소 제거

- contains(Object) : 포함여부확인

- size() : 크기 반환

- clear() : 전체 삭제

- isEmpty() : 비었는지 확인

- iterator() : 반복자 확인

- forEach(Consumer) : 요소 모두 순회

### 동기화 처리

컬렉션은 비동기 처리를 기본으로 한다.

멀티스레드 환경에서는 그러므로

    List<String> syncList = Collections.synchronizedList(new ArrayList<>());

이렇게 처리해야 안전하다.

### 불변 컬렉션

List.of(), Set.of() 등으로 불변 컬렉션을 생성할 수 있다.

### 상황별 컬렉션 사용

- 순서 유지, 중복 허용 : ArrayList

- 빠른 검색, 중복 검색 : HashSet

- 키-값 저장 : HashMap

- 정렬된 키-값 저장 : TreeMap

- 삽입/삭제 많고 순서를 유지 : LinkedList

- 멀티스레드 보안 : ConcurrentHashMap, CopyOnWriteArraryList 등