a, b, c = map(int, input().split())

if 1 <= a <= 1000000 and 1 <= b <= 1000000 and 1 <= c <= 1000000 and a != b and b != c and a != c:
    if a > b :
        a, b = b, a
    
    if b > c :
       b, c = c, b

    if a > b :
        a, b = b, a
    
    print(f"{a} {b} {c}")