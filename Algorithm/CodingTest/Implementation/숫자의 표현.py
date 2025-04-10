import sys

def solution(n):
    count = 1
    for i in range(1, n):
        sum = i
        is_first = True
        for j in range(i+1, n):
            sum += j
            if is_first and sum > n:
                break
            if sum == n:
                count += 1
                break
    return count

n = int(sys.stdin.readline().strip())
print(solution(n))