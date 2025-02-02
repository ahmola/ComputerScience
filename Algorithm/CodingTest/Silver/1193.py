n = int(input(""))
sum = 0
level = 0

for i in range(1, n+1) :
    if sum >= n :
        break
    else :
        sum += i
        level = i

d = sum - n

if level % 2 == 0 :
    print(f"{level-d}/{1+d}")
else :
    print(f"{1+d}/{level-d}")