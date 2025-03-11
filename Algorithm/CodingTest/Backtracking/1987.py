from itertools import product

def alpha(x, y, visited, count):
    global max_move
    max_move = max(max_move, count)
    movement = [[1,0], [0,1], [-1, 0], [0, -1]]

    for dx, dy in movement:
        x, y = x+dx, y+dy
        if 0 <= x < c and 0 <= y < r and alphabet[y][x] not in visited:
            alpha(x, y, visited | {alphabet[y][x]}, count+1)

r, c = map(int,input().split(" "))
alphabet = [list(input()) for _ in range(r)]
max_move = 0
alpha(0,0,{alphabet[0][0]}, 1)
print(max_move)