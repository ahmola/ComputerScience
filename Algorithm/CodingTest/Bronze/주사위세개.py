a, b, c = map(int, input().split())

if 1 <= a <= 6 and 1 <= b <= 6 and 1 <= c <= 6 :
    
    if a == b and b == c :
        print(10000 + a * 1000)
    elif a == b :
        print(1000 + a * 100)
    elif a == c :
        print(1000 + a * 100)    
    elif c == b :
        print(1000 + b * 100)
    else :
        dice = [a, b, c]
        print(int(max(dice)*100))
