import sys
import heapq

t = int(sys.stdin.readline().strip())
result = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    heap = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(heap)
    sum = 0
    while len(heap) > 1:
        x, y = heapq.heappop(heap), heapq.heappop(heap)
        sum += (x+y)
        heapq.heappush(heap, x+y)

    result.append(sum)

for r in result: print(r)