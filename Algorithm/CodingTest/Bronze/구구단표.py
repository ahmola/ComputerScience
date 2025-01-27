n = int(input())
found = False

if 1 <= n <= 100 :
    for i in range(2, 10) :
        if n == 5 :
            found = True
            break

        for j in range(1, 10) :
            if n == j or n == i*j:
                found = True
                break
            
        if found :
            break

print(1 if found else 0)