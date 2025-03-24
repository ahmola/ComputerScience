import sys
import heapq
sys.setrecursionlimit(10**6)

def dijkstra(graph, start, n):
    distance = [float("inf")]*(n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist+1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))

    return distance

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = dijkstra(graph, x, n)
is_not_have = True
for i in range(n+1):
    if result[i] == k:
        is_not_have = False
        print(i)

if is_not_have:
    print(-1)
