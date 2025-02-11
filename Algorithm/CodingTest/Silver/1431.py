# 1. 길이가 짧은 것부터
# 2. 길이가 같다면 숫자만을 더해서 더 작은 것을 먼저
# 3. 숫자와 알파벳(아스키 코드로 변경)하여 사전순으로 나열
# 조건들을 더해서 딕셔너리 키로 사용

t = int(input())
serial_number = [list(input()) for _ in range(t)]
serial_dict = {}

for s in serial_number :
    # 1번 조건
    leng = len(s)

    # 2번 조건
    numbers = list(map(int, ''.join(filter(str.isdigit, s))))
    count2 = 0
    for n in numbers :
        count2 += n
    # 3번 조건
    chars = list(''.join(filter(str.isalpha, s)))
    count3 = 0
    for c in chars :
        count3 += ord(c)
    
    if leng not in serial_dict :
        serial_dict[leng] = []
    serial_dict[leng].append(s)

for s in sorted(serial_dict.items()) : print(''.join(s[1][0]))