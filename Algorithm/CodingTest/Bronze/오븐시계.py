a, b = map(int, input().split())
c = int(input())

total = a * 60 + b + c

a = total // 60
total = total % 60
if a >= 24 :
    a -= 24

b = total
if b >= 60 :
    b -= 60

print(f"{a} {b}")