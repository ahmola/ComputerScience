n = int(input())
number = list(map(int, input().split(" ")))
indexes = []

for i in range(n):
    index = 0
    for j in range(n):
        if number[i] > number[j]:
            index += 1
    indexes.append(index)

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if number[i] == number[j]:
            indexes[i] += 1

for i in indexes : print(i, end=" ")
print()