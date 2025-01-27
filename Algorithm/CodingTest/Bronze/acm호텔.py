t = int(input(""))
result = []

for _ in range(t) :
    h, w, n = map(int, input().split())
    
    # yyxx 층
    
    if n % h == 0 :
        y = h
        x = n // h
    else :
        y = n % h 
        x = n // h + 1
    
    str_x = str(x)
    str_y = str(y)

    if x < 10 :
        str_x = "0" + str(x)
    
    result.append(int(str_y + str_x))

for r in result :
    print(r)