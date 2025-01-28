t = int(input(""))
result = []
example = [[1], [2,4,8,6], [3, 9, 7, 1], [4,6], [5], [6], [7,9,3,1], [8,4,2,6], [9, 1], [10]]

for _ in range(t) :
    a, b = map(int, input().split())
    l = len(example[a%10-1])
    if b % l != 0 :
        result.append(example[a%10-1][(b % l)-1])
    else :
        result.append(example[a%10-1][-1])

for r in result : print(r)