n = int(input(""))

r = list(map(int, input().split()))

if n == 1 :
    print(r[0] ** 2)
else :
    print(min(r) * max(r))