import sys
def dfs(wood, x, y):
    if wood[y][x] == "-":
        wood[y][x] = "x"
        if x-1 >= 0 and wood[y][x-1] == "-":
            dfs(wood, x-1, y)
        if x+1 < len(wood[0]) and wood[y][x+1] == "-":
            dfs(wood, x+1, y)
    else:
        wood[y][x] = "x"
        if y-1 >= 0 and wood[y-1][x] == "|":
            dfs(wood, x, y-1)
        if y+1 < len(wood) and wood[y+1][x] == "|":
            dfs(wood, x, y+1)

n, m = map(int, sys.stdin.readline().split())
wood = [list(sys.stdin.readline().strip()) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        if wood[i][j] != "x":
            dfs(wood, j, i)
            count += 1

print(count)