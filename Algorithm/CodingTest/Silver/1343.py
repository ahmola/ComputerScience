poly = input("")
x = poly.split(".")
x = [x1 for x1 in x if x1 != ""]
is_poly = True

result = []
for x1 in x :
    if len(x1) % 2 != 0:
        is_poly = False
        print(-1)
        break
    elif len(x1) == 2 :
        x1 = "BB"
    else :
        if len(x1) % 4 != 0:
            x1 = "A"*(len(x1)-2)
            x1 += "BB"
        else :
            x1 = "A"*len(x1)
    result.append(x1)

if is_poly :
    index = 0
    i = 0
    while i < len(poly) :
        if poly[i] == "X" :
            print(result[index], end="")
            i += len(result[index])-1
            if index+1 < len(result) :
                index += 1
        else :
            print(poly[i], end="")
        i += 1