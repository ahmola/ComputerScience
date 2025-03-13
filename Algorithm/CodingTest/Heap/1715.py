import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = [int(sys.stdin.readline().strip()) for _ in range(n)]
heapq.heapify(heap)
sum = 0
while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    sum += (x+y)
    heapq.heappush(heap, x+y)

print(sum)