n = int(input(""))

if n == 1:
    file_name = input("")
    print(file_name)
else :
    files = list(input("") for _ in range(n))
    l = len(files[0])
    result = ""

    for i in range(l) :
        is_same = True
        for j in range(1, n) :
            if files[0][i] != files[j][i] :
                is_same = False
                result = result + "?"
                break
        if is_same :
            result = result + files[0][i]

    print(result)