# 15, 28, 19를 등차로 하는 등차수열들에 각각 e,s,m의 값을 더하면 됨
e,s,m = map(int, input().split())

en = set((15*x+e) for x in range(10000))
sn = set((28*x+s) for x in range(10000))
mn = set((19*x+m) for x in range(10000))

# 세 항에 모두 존재하는 값을 출력
common = set.intersection(*[en,sn,mn])
common = list(common)
common.sort()

print(common[0])