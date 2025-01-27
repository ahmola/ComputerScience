sum, min = map(int, input().split())

if 0 <= sum <= 1000 and 0 <= min <= 1000 :
    a = (sum + min) // 2
    b = (sum - min) // 2
    if (sum + min) % 2 == 0 and (sum - min) % 2 == 0 and a >= 0 and b >= 0 :
        if a >= b :
            print(f"{a} {b}")
        else :
            print(f"{b} {a}")

    else :
        print("-1")