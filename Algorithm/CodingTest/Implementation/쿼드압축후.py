import sys

def solution(arr):
    length= len(arr[0])
    half = len(arr[0])//2
    result = [0, 0]

    if all(all(x==0 for x in row) for row in arr):
        return [1, 0]
    elif all(all(x==1 for x in row) for row in arr):
        return [0, 1]

    # 1사분면
    first = [row[0:half] for row in arr[0:half]]
    if all(all(x == 0 for x in row) for row in first):
        result[0] += 1
    elif all(all(x == 1 for x in row) for row in first):
        result[1] += 1
    else :
        sub = solution(first)
        result[0] += sub[0]
        result[1] += sub[1]
    # 2사분면
    second = [row[half:length] for row in arr[0:half]]
    if all(all(x == 0 for x in row) for row in second):
        result[0] += 1
    elif all(all(x == 1 for x in row) for row in second):
        result[1] += 1
    else:
        sub = solution(second)
        result[0] += sub[0]
        result[1] += sub[1]
    # 제3사분면
    third = [row[0:half] for row in arr[half:length]]
    if all(all(x == 0 for x in row) for row in third):
        result[0] += 1
    elif all(all(x == 1 for x in row) for row in third):
        result[1] += 1
    else:
        sub = solution(third)
        result[0] += sub[0]
        result[1] += sub[1]
    # 제4사분면
    fourth = [row[half:length] for row in arr[half:length]]
    if all(all(x == 0 for x in row) for row in fourth):
        result[0] += 1
    elif all(all(x == 1 for x in row) for row in fourth):
        result[1] += 1
    else:
        sub = solution(fourth)
        result[0] += sub[0]
        result[1] += sub[1]

    return result

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solution(arr))