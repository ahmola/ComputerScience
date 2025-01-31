# 도데체 시간제한을 왜 둔건지 이해할 수 없다. 그렇다고 c/c++로 바꾼다고 시간초과가 해결되진 않는다

import math

n = int(input(""))
q = [list(map(int, input().split())) for _ in range(n)]

m = int(input(""))
r = [list(map(int, input().split())) for _ in range(m)]

result = [0] * m

for i in range(m) :
    for j in range(n) :
        if r[i][0] - r[i][3] <= q[j][0] <= r[i][0] + r[i][3] and r[i][1] - r[i][3] <= q[j][1] <= r[i][1] + r[i][3] and r[i][2] - r[i][3] <= q[j][2] <= r[i][2] + r[i][3] :
            if pow(r[i][0] - q[j][0],2) + pow(r[i][1] - q[j][1],2) + pow(r[i][2] - q[j][2],2) <= pow(r[i][3],2) :
                result[i] += 1
            
for r in result : print(r)