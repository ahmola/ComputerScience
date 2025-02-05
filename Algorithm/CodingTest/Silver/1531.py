# 100x100 좌표를 만든 후 각 좌표별로 겹치는 횟수를 세면 됨. 점을 세는 문제는 일단 전체 좌표를 만들고 해당 범위에 해당 할 때마다 카운트
n, m = map(int, input().split())
grid = [[0]*101 for _ in range(101)]

for _ in range(n) :
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1) :
        for j in range(y1, y2+1) :
            grid[i][j] += 1
    
result = sum(1 for i in range(101) for j in range(101) if grid[i][j] > m)

print(result)