import sys

def dfs(virus, start, visited):
    visited[start-1] = True
    count = 1
    for i in virus[start]:
        if not visited[i-1]:
            count += dfs(virus, i, visited)
    
    return count

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
visited = [False]*n
virus = [[] for _ in range(n+1)]

for _ in range(k):
    u, v = map(int, sys.stdin.readline().split())
    virus[u].append(v)
    virus[v].append(u)

print(dfs(virus, 1, visited)-1)