import sys
sys.setrecursionlimit(10**6)

def dfs(territory, x, y):
    territory[y][x] = True
    size = 1

    for dx, dy in [[1,0], [-1, 0], [0, 1], [0 , -1]]:
        nx, ny = dx+x, dy+y
        if 0 <= nx < len(territory[y]) and 0 <= ny < len(territory) and not territory[ny][nx]:
            size += dfs(territory, nx, ny)
    
    return size

def square(points, n, m):
    territory = [[False]*m for _ in range(n)]

    for x1,y1, x2, y2 in points:
        for i in range(y1, y2):
            for j in range(x1, x2):
                if not territory[i][j]:
                    territory[i][j] = True

    target = []
    for i in range(n):
        for j in range(m):
            if not territory[i][j]:
                target.append([j, i])

    count = 0
    size = []
    for t in target:
        x, y = t[0], t[1]
        if not territory[y][x]:
            size.append(dfs(territory, x, y))
            count += 1

    return [count , size]


n, m , k = map(int , sys.stdin.readline().split())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

result = square(points, n, m)
result[1].sort()
print(result[0])
print(*result[1])