six = "666"

n = int(input(""))
result = []

for i in range(666, 100000000) :
    if len(result) == n :
        break
    if six in str(i) :
        result.append(i)

result.sort()
print(result[n-1])