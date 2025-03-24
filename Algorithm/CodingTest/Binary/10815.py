import sys

n = int(sys.stdin.readline().strip())
sanguen = list(map(int, sys.stdin.readline().split()))
sanguen.sort()
m = int(sys.stdin.readline().strip())
given = list(map(int, sys.stdin.readline().split()))
result = [0]*m

for i in range(m):
    left, right = 0, n-1

    while left <= right:
        mid = (left+right)//2
        
        if sanguen[mid] == given[i]:
            result[i] = 1
            break

        if sanguen[mid] < given[i]:
            left = mid+1
        else:
            right = mid-1

print(*result)