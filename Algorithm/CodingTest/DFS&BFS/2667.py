import sys
sys.setrecursionlimit(10**6)
def dfs(apartment, x, y):
    apartment[y][x] = "0"
    count = 1

    for dx, dy in [[1,0], [-1, 0], [0, 1], [0, -1]]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(apartment[y]) and 0 <= ny < len(apartment) and apartment[ny][nx] == "1":
            count += dfs(apartment, nx, ny)

    return count

n = int(sys.stdin.readline().strip())
apartment = [list(sys.stdin.readline().strip()) for _ in range(n)]
count = 0
apart = []

for i in range(n):
    for j in range(n):
        if apartment[i][j] == "1":
            apart.append(dfs(apartment, j, i))
            count += 1
    
print(count)
apart.sort()
for a in apart: print(a)