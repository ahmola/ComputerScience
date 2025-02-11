import math
t = int(input())
points = [list(map(int, input().split())) for _ in range(t)]
result = []
for p in points :
    d = math.sqrt((p[0]-p[3])**2+(p[1]-p[4])**2)
    if d == 0 and p[2] - p[5] == 0 :
        result.append(-1)
    elif d > p[2] + p[5] :
        result.append(0)
    elif d == p[2]+p[5] or d == abs(p[2]-p[5]):
        result.append(1)
    elif d < abs(p[2]-p[5]) :
        result.append(0)
    else :
        result.append(2)
for r in result : print(r)