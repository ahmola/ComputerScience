import sys

n = int(sys.stdin.readline().strip())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()
result = [0, 0]
min_sum = float("Inf")

left, right = 0, n-1

while left < right:
    liquid_sum = liquid[left]+liquid[right]

    if abs(liquid_sum) < min_sum:
        min_sum = abs(liquid_sum)
        result[0], result[1] = liquid[left], liquid[right]
    
    if liquid_sum > 0:
        right -= 1
    else :
        left += 1

print(*result)