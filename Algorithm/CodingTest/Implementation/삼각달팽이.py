import sys

def solution(n):
    limit = sum(range(1, n+1))
    num = 1
    result = [[] for _ in range(n)]
    for i in range(1, n+1):
        for _ in range(i):
            result[i-1].append(0)
    leng = n
    x, y = 0, 0

    while leng > 0 and num <= limit:
        for _ in range(leng):
            result[y][x] = num
            num += 1
            y += 1
        x += 1
        y -= 1

        for _ in range(leng-1):
            result[y][x] = num
            num += 1
            x += 1
        x -= 2
        y -= 1

        for _ in range(leng-2):
            result[y][x] = num
            num += 1
            y -= 1
            x -= 1
        x += 1
        y += 2

        leng -= 3
    return sum(result, [])

n = int(sys.stdin.readline().strip())
print(solution(n))