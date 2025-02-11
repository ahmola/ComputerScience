from typing import Counter

name = input()
# counter로 딕셔너리를 만들어서 문자열의 문자 수를 세고 sorted()를 사용하여 정렬
name = sorted(Counter(name).items())

is_pell = True
half_pell = []
odd_char = ''
for char, count in name :
    # 홀수 개의 문자는 하나만 존재해야 함
    if count % 2 != 0 :
        if odd_char :
            is_pell = False
            print("I'm Sorry Hansoo")
            break
        odd_char = char
    # 나머지 문자는 짝수 개이다. 팰린드롬은 데칼코마니처럼 뒤쪽 문자가 똑같으므로 반만 저장함
    half_pell.append(char * (count//2))

half_pell = ''.join(half_pell)

pell = ''.join(half_pell + odd_char + half_pell[::-1])

if is_pell :
    print(pell)