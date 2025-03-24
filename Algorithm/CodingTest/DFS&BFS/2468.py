import sys
sys.setrecursionlimit(10**6)

def dfs(alive, x, y):
    alive[y][x] = False
    for dx, dy in [[1,0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < n and alive[ny][nx]:
                dfs(alive, nx, ny)
    
def flood(ground, limit, n):
    alive = [[False]*n for _ in range(n)]
    target = []
    for i in range(n):
        for j in range(n):
            if ground[i][j] > limit:
                alive[i][j] = True
                target.append([j, i])
    
    count = 0
    for t in target:
        x, y = t[0], t[1]
        if alive[y][x]:
            dfs(alive, x, y)
            count += 1

    return count
    

n = int(sys.stdin.readline().strip())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_ground = 0
for g in ground:
    max_ground = max(max_ground, max(g))

count = 0
for i in range(0, max_ground+1):
    count = max(flood(ground, i, n), count)
print(count)