import math

result = []

while True :
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0 :
        break

    if a == -1 :
        if c**2 - b**2 > 0:
            a = math.sqrt(c**2 - b**2)
            result.append(["a", a])
        else :
            result.append(["Impossible.", 0])
    elif b == -1 :
        if c**2 - a**2 > 0 :
            b = math.sqrt(c**2 - a**2)
            result.append(["b", b])
        else :
            result.append(["Impossible.", 0])
    elif c == -1 :
        c = math.sqrt(a**2 + b**2)
        result.append(["c", c])
    
for i, r in enumerate(result) :
    print(f"Triangle #{i+1}")
    if r[1] == 0 :
        print(f"{r[0]}")
    else:
        print(f"{r[0]} = {r[1]:.3f}")
    print("")