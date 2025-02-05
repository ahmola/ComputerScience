def convert(chess, is_bw, n, m) :
    count = 0
    word = "WB"
    if is_bw :
        word = "BW"
    rev_word = word[1]+word[0]
    for i in range(n) :
        for j in range(0, m-2, 2) :
            if i % 2 == 0:
                if chess[i][j] + chess[i][j+1] != word :
                    chess[i][j] = word[0]
                    chess[i][j+1] = word[1]
                    count += 1
            else :
                if chess[i][j] + chess[i][j+1] != rev_word :
                    chess[i][j] = rev_word[0]
                    chess[i][j+1] = rev_word[1]
                    count += 1
    return count

n, m = map(int, input().split())
chess = list(list(input()) for _ in range(n))

# bw로 바꾸는 경우
count_bw = convert(chess, True, n, m)
count_wb = convert(chess, False, n, m)

print(count_wb)