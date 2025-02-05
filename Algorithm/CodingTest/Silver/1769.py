n = str(input())
count = 0

while len(n) > 1 :
    y = 0
    for i in n :
        y += int(i)
    n = str(y)
    count += 1

if int(n) % 3 == 0 :
    print(count)
    print("YES")
else :
    print(count)
    print("NO")