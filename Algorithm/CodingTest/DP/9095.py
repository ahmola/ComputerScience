import sys

t = int(sys.stdin.readline().strip())
testcase = [int(sys.stdin.readline().strip()) for _ in range(t)]
n = max(testcase)+1
memo = [0]*n
memo[1] = 1
memo[2] = 2
memo[3] = 4

# 마지막에 1, 2, 3을 더하는 경우의 수를 모두 더한다고 생각하면 된다.
# 즉, 4일때 3을 만드는 모든 경우의 수에 1을 만드는 경우의 수를 더하고
# 2를 만드는 경우의 수에 2를 만드는 경우의 수를 더한 경우의 수
# 1을 만드는 경우의 수에 3을 만드는 경우의 수를 더하는 경우의 수
for i in range(4, n):
    memo[i] = memo[i-1]+memo[i-2]+memo[i-3]

for t in testcase:
    print(memo[t])