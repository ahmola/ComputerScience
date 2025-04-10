import sys

def solution(rows, columns, queries):
    rowcol = [[] for _ in range(rows)]
    num = 0
    result = []

    for r in range(rows):
        for c in range(columns):
            num += 1
            rowcol[r].append(num)

    for query in queries:
        c_x, c_y = query[1]-1, query[0]-1
        s_x, s_y = query[1]-1, query[0]-1
        e_x, e_y = query[3]-1, query[2]-1
        current, next = rowcol[c_y][c_x], 0
        min_result = rowcol[c_y][c_x]

        while c_x < e_x:
            c_x += 1
            next = rowcol[c_y][c_x]
            rowcol[c_y][c_x] = current
            current = next
            min_result = min(min_result, rowcol[c_y][c_x])
        while c_y < e_y:
            c_y += 1
            next = rowcol[c_y][c_x]
            rowcol[c_y][c_x] = current
            current = next
            min_result = min(min_result, rowcol[c_y][c_x])
        while c_x > s_x:
            c_x -= 1
            next = rowcol[c_y][c_x]
            rowcol[c_y][c_x] = current
            current = next
            min_result = min(min_result, rowcol[c_y][c_x])
        while c_y > s_y:
            c_y -= 1
            next = rowcol[c_y][c_x]
            rowcol[c_y][c_x] = current
            current = next
            min_result = min(min_result, rowcol[c_y][c_x])

        result.append(min_result)

    return result

rows, columns, n = map(int, sys.stdin.readline().split())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solution(rows, columns, queries))