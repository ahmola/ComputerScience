import sys
sys.setrecursionlimit(10**6)

def dfs(painting, x, y):
    painting[y][x] = 0
    size = 1
    for dx, dy in [[1,0], [-1,0], [0, -1], [0, 1]]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(painting[0]) and 0 <= ny < len(painting) and painting[ny][nx] == 1:
            size += dfs(painting, nx, ny)
    return size

n, m = map(int, sys.stdin.readline().split())
painting = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if painting[i][j] == 1:
            max_size = max(dfs(painting, j, i), max_size)
            count += 1

print(count)
print(max_size)