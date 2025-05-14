# Stream API

Collections 타입을 상속하는 데이터형들을 함수형 스타일로 처리하게 해주는 도구이다. Declarative 스타일로 데이터를 필터링, 매핑, 정렬, 집계할 수 있다.

파이프라인 구조로, 데이터를 순차적/병렬적으로 처리한다.

## 기본 구조

    Collection -> Stream 생성 -> 중간 연산(stream변형, lazy execution, 최종 연산 호출 전까지 반환하지 않음) -> 최종 연산(stream을 닫고 결과 반환, 더 이상 stream사용 불가능)

## 자주 사용되는 중간 연산들

    - filter(Predicate) : 조건에 맞는 데이터만 남김
    ex) filter(data -> data.length() > 3)

    - map(Function) : 데이터를 다른 값으로 반환
    ex) map(String::toUpperCase)

    - flatMap(Function) : 다차원 스트림 평탄화
    ex) flatMap(list -> list.stream())

    - sorted()/sorted(Comparator) : 정렬

    - distinct() : 중복 제거

    - limit(n) : 최대 n개 추출

    - skip(n) : 처음 n개 건너뜀

    - peek(Consumer) : 디버깅, 데이터들을 훑어봄
    ex) peek(System.out::println), 데이터출력

## 자주 사용되는 최종 연산

    - forEach(Consumer) : 각 데이터에 대한 작업 수행

    - collect(Collectors) : 컬렉션 수집
    ex) collect(Collectors.toList())

    - toArray() : 배열로 변환

    - reduce(BinaryOperator) : 데이터 누적 연산
    ex) reduce(0, Integer::sum)

    - count() : 데이터 개수