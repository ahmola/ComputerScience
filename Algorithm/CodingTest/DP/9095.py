import sys
from itertools import combinations

def dp(number):
    for comb in combinations():
        heapq

t = int(sys.stdin.readline().strip())
testcase = [int(sys.stdin.readline().strip()) for _ in range(t)]
memo = [[] for _ in range(max(testcase)+1)]

for test in testcase:
    print(dp(test))