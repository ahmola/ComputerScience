n = int(input())

result = []

if 1 <= n <= 100 :
    for _ in range(n) :
        a, b = map(int, input().split())
        if a <= b :
            result.append(b)

    if len(result) == 0 :
        print(-1)
    else :
        print(min(result))
