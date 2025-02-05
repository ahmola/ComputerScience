n = list(input(""))
count = [0] * 10

n.sort()
n = [int(x) for x in n]

for i in n :
    count[i] += 1
count[6] = (count[6]+count[9])
if count[6] % 2 != 0 : count[6] = count[6]/2 + 1 
else : count[6] = count[6]/2
count[9] = count[6]

print(int(max(count)))