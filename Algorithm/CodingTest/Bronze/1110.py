a = int(input(""))
ans = str(a // 10) + str(a % 10)

c = a//10+a%10
p = str(a%10) + str(c%10)

n = 1
while ans != p :
    c = int(p)//10 + int(p) % 10
    p = str(int(p)%10) + str(c%10)
    n += 1

print(n)