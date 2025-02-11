def convert(chess_origin, n, m) :
    count_bw = [0]*((m-7)*(n-7))
    count_wb = [0]*((m-7)*(n-7))
    chess_bw = [[("B" if (i + j) % 2 == 0 else "W") for j in range(8)] for i in range(8)]
    chess_wb = [[("W" if (i + j) % 2 == 0 else "B") for j in range(8)] for i in range(8)]

    index_bw = 0
    for i in range(n-7) :
        for j in range(m-7) :
            for k in range(8) :
                for p in range(8) :
                    if chess_origin[i+k][j+p] != chess_bw[k][p] :
                        count_bw[index_bw] += 1
            index_bw += 1

    index_wb = 0
    for i in range(n-7) :
        for j in range(m-7) :
            for k in range(8) :
                for p in range(8) :
                    if chess_origin[i+k][j+p] != chess_wb[k][p] :
                        count_wb[index_wb] += 1
            index_wb += 1
    
    return min(min(count_bw), min(count_wb))

n, m = map(int, input().split())
chess = list(list(input()) for _ in range(n))

print(convert(chess, n, m))