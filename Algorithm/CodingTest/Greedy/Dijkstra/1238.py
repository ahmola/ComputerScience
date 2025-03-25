import sys
import heapq

def dijkstra(graph, start, n):
    distance = [float("inf")] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start)) # 최소거리, 목적지

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next_node, next_distance in graph[now]:
            cost = next_distance + dist

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    for i in range(1, n+1):
        if i == start:
            continue
        start_distance = [float("inf")]*(n+1)
        start_distance[i] = 0
        heapq.heappush(queue, (0, i))

        while queue:
            dist, now = heapq.heappop(queue)

            if start_distance[now] < dist:
                continue

            for next_node, next_distance in graph[now]:
                cost = next_distance+dist

                if cost < start_distance[next_node]:
                    start_distance[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))
        distance[i] += start_distance[start]

    return distance

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

result = dijkstra(graph, x, n)[1:]

print(max(result))