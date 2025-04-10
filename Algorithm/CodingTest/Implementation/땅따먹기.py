import sys

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)
    return max(land[-1])

n = int(sys.stdin.readline().strip())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solution(land))