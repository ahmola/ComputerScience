n, m = map(int, input().split())

square = [list(map(int, input())) for _ in range(n)]
min_side = min(n, m)
min_square = 1

for i in range(n) :
    for j in range(m) :
        for k in range(min_side, 0, -1) :
            if (i+k < n and j+k < m) and (square[i][j] == square[i+k][j] == square[i][j+k] == square[i+k][j+k]) :
                min_square = max(min_square, (k+1)**2)

print(min_square)