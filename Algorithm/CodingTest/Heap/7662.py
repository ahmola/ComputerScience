# 지피티가 풀어도 틀리고 내가 풀면 시간 초과면 어쩌라는건지 모르겠다.
import sys
import heapq

t = int(sys.stdin.readline().strip())

for _ in range(t):
    min_heap = []
    max_heap = []
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        case = sys.stdin.readline().split()
        x = int(case[1])
        
        if case[0] == "I":
            heapq.heappush(min_heap, x)
            heapq.heappush(max_heap, -x)
        elif x == 1 and max_heap:
            rem = heapq.heappop(max_heap)
            min_heap.remove(-rem)
        elif x == -1 and min_heap:
            rem = heapq.heappop(min_heap)
            max_heap.remove(-rem)

    if not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])