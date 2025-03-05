# from copy import deepcopy
# from itertools import combinations, permutations

# def lamp_on(lamp, m):
#     for i in range(len(lamp)):
#         lamp[i][m] ^= 1

# n, m = map(int, input().split(" "))
# lamp = [[int(d) for d in input()] for _ in range(n)]
# k = int(input())

# count = [0]
# count_index = 0
# turn_on = []

# # 조합을 사용하여 각 열을 키는 수를 정함
# for comb in combinations(range(k+1), m):
#     if sum(comb) == k:
#         t = list(map(int, comb))
#         turn_on.append([list(p) for p in list(permutations(t))])
    
# turn_on = sum(turn_on, [])
# for t in turn_on :
#     copy_lamp = deepcopy(lamp)
#     # 조합에 따라 열을 킴
#     for i in range(m):
#         for _ in range(t[i]):
#             lamp_on(copy_lamp, i)

#     # 켜진 행의 수를 셈
#     for i in range(n):
#         is_on = True
#         for j in range(m):
#             if copy_lamp[i][j] == 0:
#                 is_on = False
#                 break
#         if is_on:
#             count[count_index] += 1

#     count.append(0)
#     count_index += 1

# print(max(count))
from collections import Counter

n, m = map(int, input().split())
lamp = [input().strip() for _ in range(n)]
k = int(input())

# 같은 행 패턴을 그룹화하여 몇 개씩 존재하는지 확인
row_count = Counter(lamp)

max_on_rows = 0

# 각 행 패턴에 대해 가능한 스위치 조작 여부 확인
for row, cnt in row_count.items():
    zero_count = row.count('0')  # 0의 개수 확인

    # 스위치를 정확히 K번 누를 수 있는 경우 (0의 개수 <= K, 그리고 같은 패턴이 유지될 수 있는 경우)
    if zero_count <= k and (k - zero_count) % 2 == 0:
        max_on_rows = max(max_on_rows, cnt)

print(max_on_rows)