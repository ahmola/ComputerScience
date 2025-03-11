from itertools import combinations, product

def available(chess, i, j, n):
    chess[i][j] = 1

    for p in range(j+1, n):
        chess[i][p] = 1

    for p in range(j-1, -1, -1):
        chess[i][p] = 1

    for q in range(i+1, n):
        chess[q][j] = 1

    for q in range(i-1, -1, -1):
        chess[q][j] = 1
    
    r, s = i+1, j+1
    while r < n and s < n:
        chess[r][s] = 1
        r += 1
        s += 1
    
    r, s = i+1, j-1
    while r < n and s >= 0:
        chess[r][s] = 1
        r += 1
        s -= 1

    r, s = i-1, j+1
    while r >= 0 and s < n:
        chess[r][s] = 1
        r -= 1
        s += 1
    
    r, s = i-1, j-1
    while r >= 0 and s >= 0:
        chess[r][s] = 1
        r -= 1
        s -= 1

def n_queen(n):
    count = 0
    chess = [[0]*n for _ in range(n)]

    coordinate = [[x,y] for x,y in product(range(n), range(n))]
    for coor in combinations(coordinate, n):
        coor = list(coor)
        queens = n
        moc_chess = [row[:] for row in chess]

        for c in coor:
            x, y = c[0], c[1]
            if moc_chess[y][x] == 0:
                available(moc_chess, y, x, n)
                queens -= 1
                if queens == 0:
                    for c in coor: print(c, end=" ")
                    print()
                    count += 1
                    break

    return count

n = int(input())
print(n_queen(n))