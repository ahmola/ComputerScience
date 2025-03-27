import sys

def w(a,b,c):
    if memo[a][b][c] != 0:
        return memo[a][b][c]
    if a < b < c:
        memo[a][b][c] =  w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return memo[a][b][c]
    else:
        memo[a][b][c] = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return memo[a][b][c]

numbers = []
while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    numbers.append([a,b,c])
# -50~50 => 0~100
memo = [[[0]*101 for _ in range(101)] for _ in range(101)]
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i <= 50 or j <= 50 or k <= 50:
                memo[i][j][k] = 1

w(70,70,70)
for i in range(51, 101):
    for j in range(51, 101):
        for k in range(51, 101):
            if i > 70 or j > 70 or k > 70:
                memo[i][j][k] = memo[70][70][70]

for n in numbers:
    a,b,c = n[0], n[1], n[2]
    print(f"w({a}, {b}, {c}) = {w(a+50,b+50,c+50)}")