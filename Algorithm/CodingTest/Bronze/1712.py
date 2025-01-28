a, b, c = map(int, input().split())
i = 1
if b >= c :
    print(-1)
else :
    i = a/(c-b)
    print(int(i)+1)