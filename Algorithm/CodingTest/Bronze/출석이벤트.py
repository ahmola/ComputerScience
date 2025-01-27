n = int(input(""))
p = int(input(""))

v = []

if 0 <= n <= 30 and 100 <= p <= 50000 and p % 100 == 0 :
    
    if n >= 20 :
        v.append(int(p * 0.75))
    
    if n >= 15 :
        if p - 2000 >= 0 :
            v.append(p - 2000)
        else :
            v.append(0)
    
    if n >= 10 :
        v.append(int(p * 0.9))

    if n >= 5 :
        if p - 500 >= 0 :
            v.append(p - 500)
        else :
            v.append(0)
    else :
        v.append(p) 
    
    print(min(v))