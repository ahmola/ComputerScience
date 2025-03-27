import sys

def dp(number):
    if memo[number] != 0:
        return memo[number]

    memo[number] = (dp(number-1) + dp(number-2) + dp(number-3))%(1000000009)
    return memo[number]

t = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(t)]
memo = [0]*(10**6+1)
memo[1] = 1
memo[2] = 2
memo[3] = 4
for i in range(1, max(numbers)+1):
    dp(i)

for n in numbers:
    print(memo[n])