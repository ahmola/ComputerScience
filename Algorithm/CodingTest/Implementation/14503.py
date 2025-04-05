import sys

def simulate(n, m, y, x, d):
    count = 0
    move = [(-1,0), (0,1), (1,0), (0, -1)]
    # 2를 청소되었음으로 가정
    if room[y][x] == 0:
        count += 1
        room[y][x] = 2

    for _ in range(4):
        d = d-1 if d > 0 else 3
        dy, dx = move[d]
        nx, ny = dx+x, dy+y
        # 청소가 안되어있다면
        if 0 <= nx < m and 0 <= ny < n and room[ny][nx] == 0:
            count += simulate(n, m, ny, nx, d)
            return count

    nd = (d+2)%4
    nx, ny = x+move[nd][1], y+move[nd][0]
    if 0 <= nx < m and 0 <= ny < n and room[ny][nx] != 1:
        count += simulate(n, m, ny, nx, d)
    return count

n, m = map(int , sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(simulate(n,m,r,c,d))
# for y in range(n):
#     for x in range(m):
#         print(room[y][x], end=" ")
#     print()