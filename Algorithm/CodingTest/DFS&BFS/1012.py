import sys
sys.setrecursionlimit(10**6)
def dfs(baechu, x, y):
    move = [[1,0], [-1, 0], [0, 1], [0, -1]]
    baechu[y][x] = False

    for dx, dy in move:
        if 0 <= dx+x < len(baechu[0]) and 0 <= dy+y < len(baechu) and baechu[dy+y][dx+x]:
            dfs(baechu, dx+x, dy+y)
        

t = int(sys.stdin.readline().strip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    baechu = [[False]*m for _ in range(n)]
    count = 0

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        baechu[y][x] = True
    
    for i in range(n):
        for j in range(m):
            if baechu[i][j]:
                dfs(baechu, j, i)
                count += 1
    
    print(count)