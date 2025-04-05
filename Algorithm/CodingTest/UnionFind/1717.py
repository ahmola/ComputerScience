import sys

def find(key):
    if key != unions[key]:
        unions[key] = find(unions[key])
    return unions[key]

def union(a, b):
    p1, p2 = find(a), find(b)

    if p1 > p2:
        unions[p2] = p1
    elif p1 < p2:
        unions[p1] = p2

def check(a, b):
    return find(a) == find(b)

n, m = map(int, sys.stdin.readline().split())
sets = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
unions = {}
for i in range(0, n+1):
    unions[i] = i

result = []
for s in sets:
    op, a, b = s[0], s[1], s[2]
    if op == 1:
        result.append("YES" if check(a, b) else "NO")
    else:
        union(a,b)

for r in result:
    print(r)