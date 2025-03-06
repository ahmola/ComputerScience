n = int(input())

dungchi = [list(map(int, input().split(" "))) for _ in range(n)]
count = [1]*n

for i in range(n):
    for j in range(n):
        if i != j and dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
            count[i] += 1

for c in count:
    print(c, end=" ")