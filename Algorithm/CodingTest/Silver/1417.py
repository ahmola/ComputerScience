def steal(a, b):
    return int(abs(a-b)/2)+1

t = int(input(""))
result = [int(input()) for _ in range(t)]

cand = result[1:]

if t == 1 :
    print(0)
else :
    count = 0 
    while result[0] <= max(cand) :
        i = cand.index(max(cand))
        result[0] += 1
        cand[i] -= 1
        count += 1
    print(count)