import heapq
import sys

n = int(sys.stdin.readline().strip())
noodle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
noodle.sort()

heap = []

for deadline, cup in noodle:
    heapq.heappush(heap, cup)

    # heap의 길이는 곧 일수
    if deadline < len(heap):
        heapq.heappop(heap)
print(sum(heap))