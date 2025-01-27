a, b, c = map(int, input().split())

result1 = int(a * b / c)
result2 = int(a / b * c)

if result1 > result2 :
    print(result1)
else :
    print(result2)