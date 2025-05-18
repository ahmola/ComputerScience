# JavaScript Object Notation

데이터를 구조화해서 표현하기 위한 경량 텍스트 포맷

Human-Readable, Machine-Friendly, Text-Oriented의 특성을 가지며,

Javascript 문법에서 유래한 언어 독립적인 포맷이다.

기본적으로 key-value 쌍이며 2가지 구조를 가진다.

	1.	객체 (Object): { "key": value }
	2.	배열 (Array): [ value1, value2, ... ]

예시

    {
        "name": "홍길동",
        "age": 25,
        "isStudent": true,
        "skills": ["Java", "Spring", "SQL"],
        "address": {
            "city": "서울",
            "zip": "12345"
        }
    }

## 활용

- REST API 통신 : 서버-클라이언트 간에 데이터 전달

- 데이터 저장 : MongoDB같은 NoSQL류에서 문서 포맷으로 사용

- 설정 파일 : package.json같이 node.js 환경에서 사용됨

- 로그, 메시지 큐 : Kafka, Elasticsearch 등에서 JSON 형식 사용

## Parsing과 Serialize

- Serialize : 객체 -> JSON문자열 
ex) JSON.stringify(object)

- Parsing : JSON문자열 -> 객체
ex) JSON.parse(jsonStr)