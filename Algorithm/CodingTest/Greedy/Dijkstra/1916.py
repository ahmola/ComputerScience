import sys
import heapq

def dijkstra(graph, start, n):
    distance = [float("inf")] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start)) # 시작점부터 목적지까지 최소 거리, 목적지

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next_node, next_distance in graph[now]:
            cost = dist+next_distance
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return distance

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

start, end = map(int, sys.stdin.readline().split())

result = dijkstra(graph, start, n)
print(result[end])