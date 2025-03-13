# sys.stdin.realine()을 사용하면 속도가 훨씬 빨라진다. 개행문자 제거를 위해 strip()을 붙여야함
# 힙은 빠르게 최대/최소값을 찾거나 우선순위에 따른 데이터처리에 유용하게 쓰인다.
import heapq
import sys

n = int(sys.stdin.readline().strip())
heap = []

for _ in range(n):
    h = int(sys.stdin.readline().strip())
    if h == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, h)