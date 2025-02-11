# 움직임을 딕셔너리로 정의, 굳이 배열로 정의하지 않고 좌표(튜플)로 정의하여 움직인다
moves = {
    "R" : (1, 0),
    "RT" : (1, 1),
    "L" : (-1, 0),
    "LT" : (-1,1),
    "T" : (0, 1),
    "B" : (0, -1),
    "RB" : (1, -1),
    "LB" : (-1,-1)
}
# 유효한지 확인
def is_valid(x, y) :
    return 0 <= x <= 7 and 0 <= y <= 7

king, doll, n = input().split()
king_x, king_y = ord(king[0]) - 65, int(king[1]) - 1
doll_x, doll_y = ord(doll[0]) - 65, int(doll[1]) - 1
n = int(n)
move = [input() for _ in range(n)]

for m in move :
    dx, dy = moves[m]

    new_king_x, new_king_y = king_x+dx , king_y+dy

    # 움직일 수 있는지 확인
    if is_valid(new_king_x, new_king_y) :
        # 만약 돌이랑 위치가 같다면
        if new_king_x == doll_x and new_king_y == doll_y :
            # 돌이 움직일 수 없으면 그대로 놔둠
            new_doll_x, new_doll_y = doll_x+dx, doll_y+dy
            # 돌이 움직일 수 있다면
            if is_valid(new_doll_x, new_doll_y) :
                doll_x, doll_y = new_doll_x, new_doll_y
                king_x, king_y = new_king_x, new_king_y
        # 돌이랑 위치가 다르면 킹만 움직인다.
        else :
            king_x, king_y = new_king_x, new_king_y
# 재조립
king = chr(king_x+65) + str(king_y+1)
doll = chr(doll_x+65) + str(doll_y+1)

print(king)
print(doll)