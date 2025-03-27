import sys

n = int(sys.stdin.readline().strip())
cards = [0]+list(map(int, sys.stdin.readline().split()))

memo = [0]*1001
for i in range(1, n+1):
    for j in range(1, i+1):
        memo[i] = max(memo[i], memo[i-j]+cards[j])

print(memo[n])