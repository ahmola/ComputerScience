n = int(input(""))
filled = [list(input("")) for _ in range(n)]

count_x = 0
for i in range(n) :
    seat = 0
    for j in range(n) :
        if filled[i][j] != "X" and j != n-1:
            seat += 1
        else :
            # 마지막 칸에 짐이 없는 경우
            if j == n-1 and filled[i][j] == "." :
                seat += 1
            # 짐이 있는데 두 칸 이상이면
            if filled[i][j] == "X" and seat >= 2 :
                count_x += 1
                seat = 0
            # 짐이 있는데 2칸이 안되면 초기화
            elif filled[i][j] == "X" and seat < 2 :
                seat = 0
            # 마지막 칸에 짐이 없고 2칸 이상 연속이라면
            elif j == n-1 and seat >= 2:
                count_x += 1

# 방향을 바꿔서 x랑 똑같이
count_y = 0
for i in range(n) :
    seat = 0
    for j in range(n) :
        if filled[j][i] != "X" and j != n-1:
            seat += 1
        else :
            if j == n-1 and filled[j][i] == "." :
                seat += 1
            if filled[j][i] == "X" and seat >= 2 :
                count_y += 1
                seat = 0
            elif filled[j][i] == "X" and seat < 2 :
                seat = 0
            if j == n-1 and seat >= 2:
                count_y += 1

print(f"{count_x} {count_y}")