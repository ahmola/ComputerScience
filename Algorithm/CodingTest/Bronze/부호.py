result = []
test = []

for _ in range(3) :
    n = int(input(""))
    sum = 0
    for i in range(n) :
        t = int(input(""))
        test.append(t)
        sum += t
    result.append(sum)

for r in result :
    if r == 0 :
        print("0")
    elif r > 0 :
        print("+")
    elif r < 0 :
        print("-")