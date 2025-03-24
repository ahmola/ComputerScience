from collections import deque
import sys
# 최단 거리 탐색은 무조건 bfs
# 시작지점을 1로하여 가는 곳마다 해당 지점까지 이동한 거리를 모두 기록한다
def bfs(maze, target):
    queue = deque(target)

    while queue:
        x, y = queue.popleft()
        for dx, dy in [[1,0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = dx+x, dy+y
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == "1":
                maze[ny][nx] = int(maze[y][x])+1
                queue.append([nx, ny])

    return maze[len(maze)-1][len(maze[0])-1]

n, m = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(n)]
target = [[0,0]]

print(bfs(maze, target))