# 수행과 동시에 그래프의 크기가 커지는 경우에는 BFS
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def bfs(tomato, target):
    queue = deque(target)
    day = -1

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in [[1,0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = dx+x, dy+y
                if 0 <= nx < len(tomato[0]) and 0 <= ny < len(tomato) and tomato[ny][nx] == 0:
                    tomato[ny][nx] = 1
                    queue.append([nx, ny])
        day += 1
    
    return day

m,n = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
target = [[j,i] for i in range(n) for j in range(m) if tomato[i][j] == 1]
day = bfs(tomato, target)

if any(0 in row for row in tomato):
    print(-1)
else :
    print(day)