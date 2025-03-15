import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
merge = list(heapq.merge(a,b))
for i in range(n+m):
    print(heapq.heappop(merge), end=" ")