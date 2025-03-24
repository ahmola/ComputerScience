import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    p = int(sys.stdin.readline().strip())
    player = {}
    for _ in range(p):
        cost, name = map(str, sys.stdin.readline().split())
        cost = int(cost)
        player[name] = cost
    max_cost = 0
    max_name = ""
    for p in player:
        if max_cost < player[p]:
            max_cost = player[p]
            max_name = p
    print(max_name)    