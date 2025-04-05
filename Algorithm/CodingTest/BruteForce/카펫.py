import sys

def solution(brown, yellow):
    cases = []
    for i in range(1, yellow//2 + 2):
        if yellow%i == 0:
            cases.append([i, yellow//i])
            # cases.append([yellow//i, i])
    for row, col in cases:
        brown_count = 0
        carpet = [[False]*(row+2) for _ in range(col+2)]
        for i in range(col+2):
            for j in range(row+2):
                if brown_count > brown:
                    break
                if not (1 <= i <= col and 1 <= j <= row):
                    brown_count += 1
                carpet[i][j] = True
            if brown_count > brown:
                break
        if not any(False in r for r in carpet) and brown_count == brown:
            return [col+2, row+2]

b, y = map(int, sys.stdin.readline().split())

print(solution(b,y))