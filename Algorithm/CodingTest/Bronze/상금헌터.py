testcase = int(input())
result = []

for _ in range(testcase) :
    sum = 0
    a, b = map(int, input().split())
    if a == 1 :
        sum += 500
    elif 2 <= a <= 3 :
        sum += 300
    elif 4 <= a <= 6 :
        sum += 200
    elif 7 <= a <= 10 :
        sum += 50
    elif 11 <= a <= 15 :
        sum += 30
    elif 16 <= a <= 21 :
        sum += 10
    
    if b == 1 :
        sum += 512
    elif 2 <= b <= 3 :
        sum += 256
    elif 4 <= b <= 7 :
        sum += 128
    elif 8 <= b <= 15 :
        sum += 64
    elif 16 <= b <= 31 :
        sum += 32
    
    result.append(sum)

for r in result :
    r *= 10000
    print(r)