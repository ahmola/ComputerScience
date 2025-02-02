result = []

while True :
    n = input("")
    if n == "0" : break

    is_pel = True
    for i in range(len(n)//2) :
        if n[i] != n[len(n)-1-i] :
            is_pel = False
            result.append("no")
            break

    if is_pel :
        result.append("yes")

for r in result : print(r)