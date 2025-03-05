# n은 박스의 개수, m의 카드 종류의 개수
n, m = map(int, input().split(" "))
box = [list(map(int, input().split(" "))) for _ in range(n)]

# 각 카드가 몇 개의 상자에 나뉘어져 있는지 저장함
color_count = [0]*m
# 카드별 색상의 개수를 저장
color_total = [0]*m

# 박스 별로 카드 종류가 있는지 확인
for j in range(m):
    for i in range(n):
        if box[i][j] > 0:
            color_count[j] += 1
            color_total[j] += box[i][j]

moves = 0
for j in range(m):
    # 한 박스에 흩어져잇는 카드를 모두 담으려면 최소한 (한 종류의 카드를 담을 박스의 수 -1)번 움직여야함. 왜냐면 흩어져 있는 박스 중 하나에 모으면 되므로
    need_move = (color_total[j]+8)//9
    # 최대로 이동하는 경우의 수는 각 상자에서 한 종류의 카드를 전부 뽑아서 이동시키는 것
    # 즉, 한 종류의 카드가 상자 몇 개에 나누어져 있는지가 이동 횟수와 같음
    # 여기서 빼면 됨
    # 예를 들어 2개의 박스에 흩어져있고 10개가 있어서 박스가 2개가 필요하면 한 박스를 해당 종류의 카드를 담을 박스로 지정하고 옮기면 됨
    # 그러므로 흩어져잇는 2개의 박스 중에서 1개에 몰아주면 되므로 2 - 1 = 1번만 옮기면 됨
    # 해당 과정을 반복
    moves += max(0, color_count[j]-need_move)

# 조커 박스 사용
# 카드 종류가 1개 이상인 경우 조커박스를 사용하면 움직이지 않아도 됨
if m > 1:
    # 박스가 제한없이 여러 개 있어서 각 종류별로 각 박스에 담겼다고 가정(moves)
    # 근데 여기서 한 박스를 조커 박스로 지정함
    # 이 조커 박스에 제일 많이 분산되어서 이동횟수가 많은 카드를 옮김
    # 즉, 각 종류별로 각 박스에 담는 전체의 경우에서 제일 많이 분산된 카드를 조커박스로 옮긴다고 생각하고 해당 이동 수를 빼면 됨
    max_moves = max(color_count[j] - ((color_total[j]+8)//9) for j in range(m))
    moves -= max_moves

print(moves)