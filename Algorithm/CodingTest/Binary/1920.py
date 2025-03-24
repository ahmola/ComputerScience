import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
m = int(sys.stdin.readline().strip())
given = list(map(int, sys.stdin.readline().split()))
result = [0]*m

for i in range(m):
    left, right = 0, n-1
    while left <= right:
        mid = (left+right)//2
        if numbers[mid] < given[i]:
            left = mid+1
        elif numbers[mid] > given[i]:
            right = mid-1
        else:
            result[i] = 1
            break

for r in result: print(r)