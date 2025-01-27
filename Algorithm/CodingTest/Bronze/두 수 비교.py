a, b = map(int, input().split())

if -10000 <= a and b <= 10000 :
    if a > b :
        print(">")
    elif a < b :
        print("<")
    elif a == b :
        print("==")