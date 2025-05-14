# Primitive Type(기본형)

기본적인 타입으로, 실제 값 자체를 저장하는데 쓰인다.

스택이나 레지스터에 적합하며, 메모리 효율이 좋고 빠르다.

==로 값 자체를 비교한다.

가비지 컬렉션의 대상이 아님.

종류로는 int, long, float, double, boolean, char, byte, short가 있다.

# Reference Type(참조형)

실제 객체는 힙에 저장되고, 실제로 변수들이 가리키는 것은 객체가 저장된 힙의 주소를 참조하는 방식이다.

==은 참조(주소)값을 비교하고, equals()로 내용 비교

가비지 컬렉션이 관리하며 자동으로 메모리 할당이 해제된다. 이로 인해 오버헤드로 성능이 primitive보다 느리다.

종류로는, String, Integer, Object, List, 사용자 정의 클래스 등이다.

성능적인 면에서는 primitive를 쓰는 것이 맞으나, null값을 고려하여 Reference를 고려해서 사용해야 됨

예를 들어, Spring에서 Entity를 정의할 때, id의 경우 null값을 고려하여 long이 아닌 Long으로 정의함.