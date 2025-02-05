# 문제만든놈이 소수의 정의도 모른다. 초등학생도 아는 걸 소인수는 1이 되지 않는데...
n = int(input())
k = int(input())

decimal = [2, 3, 5, 7]
if n >= 11 :
    for i in range(11, n+1) :
        is_decimal = True
        for d in decimal :
            if i % d == 0:
                is_decimal = False
                break
        if is_decimal :
            decimal.append(i)

count = 0
decimal = [x for x in decimal if x > k]

for i in range(2, n+1) :
    is_k = True
    for j in decimal :
        if i % j == 0 :
            is_k = False
            break
    if is_k :
        count += 1   

print(count+1)