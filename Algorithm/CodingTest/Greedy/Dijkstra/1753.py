import sys
import heapq

def dijkstra(graph, start, v):
    distance = [float("inf")]*(v+1)
    
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

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


v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().strip())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

result = dijkstra(graph, k, v)
for i in range(1, v+1):
    if result[i] == float("inf"):
        print("INF")
    else:
        print(result[i])