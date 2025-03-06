number = int(input())

is_not_none = True
for i in range(1, 1000000):
    sum = 0
    j = i
    while j >= 10:
        sum += j % 10
        j = j // 10
    sum += j+i
    if sum == number:
        is_not_none = False
        print(i)
        break

if is_not_none :
    print(0)