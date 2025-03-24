import sys

n = int(sys.stdin.readline().strip())
n = 1000 - n
yen = [500, 100, 50 ,10 , 5 , 1]

count = 0
for y in yen:
    count += n//y
    n %= y

print(count)