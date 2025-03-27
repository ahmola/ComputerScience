import sys

one = sys.stdin.readline().strip()
two = sys.stdin.readline().strip()

one_len = len(one)
two_len = len(two)
memo = [[0]*1001 for _ in range(1001)]

for i in range(1, one_len+1):
    for j in range(1, two_len+1):
        if one[i-1] == two[j-1]:
            memo[i][j] = memo[i-1][j-1]+1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(memo[one_len][two_len])