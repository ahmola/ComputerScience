a, b, c = map(int, input().split())
time = int(input())

if 0 <= a <= 23 and 0 <= b <= 59 and 0 <= c <= 59 and 0 <= time <= 500000:
    a1 = time // 3600
    time -= a1 * 3600
    b1 = time // 60
    time -= b1 * 60
    
    a += a1
    b += b1
    c += time

    if c >= 60 :
        b += c // 60
        c = c % 60
    
    if b >= 60 :
        a += b // 60
        b = b % 60
    
    if a >= 24 :
        a = a % 24

    print(f"{a} {b} {c}")