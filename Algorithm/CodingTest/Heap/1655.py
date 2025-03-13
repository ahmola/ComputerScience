# 배열을 두개로 나누어서 하나는 최대힙과 최소힙으로 나눈다.
# 최대힙에는 작은 수들만, 최소힙에는 큰수들만 추가한다.
# 작은 수들 중에서 가장 큰 수와 비교하여 작다면 최대힙에, 크다면 최소힙에 추가한다.
# 최대힙의 길이는 항상 최소힙보다 1크게 유지한다.
import sys
import heapq

n = int(sys.stdin.readline().strip())
left_heap = []
right_heap = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())

    if not left_heap or num <= -left_heap[0]:
        heapq.heappush(left_heap, -num)
    else: 
        heapq.heappush(right_heap, num)
    
    if len(left_heap) > len(right_heap)+1:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    elif len(left_heap) < len(right_heap):
        heapq.heappush(left_heap, -heapq.heappop(right_heap))

    print(-left_heap[0])