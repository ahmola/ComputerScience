a, b = map(int, input().split())
count = 0
result = []

if a <= b :
    for i in range(a+1, b) :
        count += 1
        result.append(i)

    print(count)
    for r in result : print(r, end = " ")
else :
    for i in range(b+1, a) :
        count += 1
        result.append(i)
    
    print(count)
    for r in result : print(r, end=" ")