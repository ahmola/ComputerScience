import sys
import heapq

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    energy = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(1)
        continue
    # 쓰기전에 무조건 heapify!!!!
    heapq.heapify(energy)
    cost = 1

    for _ in range(n-1):
        x, y = heapq.heappop(energy), heapq.heappop(energy)
        sum_energy = x*y
        cost *= sum_energy
        heapq.heappush(energy, sum_energy)

    print(cost%1000000007)