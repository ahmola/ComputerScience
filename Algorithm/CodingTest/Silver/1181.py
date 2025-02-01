from operator import indexOf

n = int(input(""))

result = []
size = []

for i in range(n) :
    result.append(input(""))
    size.append(len(result[i]))

dup = list(set([x for x in size if size.count(x) > 1]))

for i in range(1, max(size)+1) :
    if i not in size :
        continue
    elif i not in dup :
        print(result[indexOf(size, i)])
    else :
        same_index = [j for j, k in enumerate(size) if k == i]
        dup_re = set()
        for s in same_index :
            dup_re.add(result[s])
        dup_re = list(dup_re)
        dup_re.sort()
        for d in dup_re :
            print(d)
