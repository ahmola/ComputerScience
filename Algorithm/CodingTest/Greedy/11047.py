import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline().strip()) for _ in range(n)]
coins.sort(reverse=True)

count = 0
for c in coins:
    count += k//c
    k %= c

print(count)