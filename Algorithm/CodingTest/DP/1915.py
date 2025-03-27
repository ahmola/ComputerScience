import sys

def dfs(square, target, n):
    for x, y in target:
        is_square = True
        for dx,dy in [[1,0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x, y
            for _ in range(n):
                nx += dx
                ny += dy
                if 0 <= nx < len(square) and 0 <= ny < len(square[0]) and square[ny][nx] == 1:
                    continue
                else:
                    is_square = False
                    break
        if is_square:
            r


n, m = map(int, sys.stdin.readline().split())
square = [list(sys.stdin.readline().strip()) for _ in range(n)]
target = []
for i in range(n):
    for j in range(m):
        if square[i][j] == 1:
            target.append([j, i])
result = 0




print(result)