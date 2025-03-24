import sys

k, n = map(int, sys.stdin.readline().split())
wire = [int(sys.stdin.readline().strip()) for _ in range(k)]

left, right = 1, max(wire)
numbers = 0
result = 0

while left <= right:
    mid = (left+right)//2
    numbers = 0
    for w in wire:
        numbers += w//mid
    
    if numbers < n:
        right = mid-1
    elif numbers >= n:
        result = mid
        left = mid+1

print(result)