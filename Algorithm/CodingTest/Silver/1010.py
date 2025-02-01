# nCr로 생각하면 된다
t = int(input())

result = []
for _ in range(t) :
    r, n = map(int, input().split())

    case = 1
    
    for i in range(r) : case *= (n-i)
    for i in range(r) : case = case // (r-i)
    result.append(case)

for r in result : print(r)