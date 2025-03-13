# heapq를 사용하여 풂
# 기본적으로 heapq는 최소힙
# 최대힙으로 사용하려면 값을 뒤집어야함. 출력도 마찬가지
# 한 줄씩 받되 가장 작은 값은 받은 줄에서 큰 값으로 교체됨
# 항상 배열의 길이를 n으로 유지
import heapq

n = int(input())
heap = []
for _ in range(n):
    row = list(map(int, input().split(" ")))
    for r in row:
        if len(heap) < n:
            heapq.heappush(heap, r)
        else:
            if heap[0] < r:
                heapq.heappushpop(heap, r)

print(heap[0])