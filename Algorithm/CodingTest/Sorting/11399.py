# 삽입 정렬
# 2번째 원소부터 시작해서 자기 앞의 원소들과 크기를 비교하며 알맞은 위치에 삽입한다.
# 앞의 원소들을 비교하는데 더 크다면 앞의 원소를 뒤로 이동시킨다.
# 가리키는 원소보다 크지 않은 원소를 마주치면 해당 원소 앞으로 값을 위치시킨다.
# 자기보다 크지 않은 원소를 만날 때까지 자기보다 큰 원소들을 앞으로 이동시킨다.
# O(n^2)
n = int(input())
number = list(map(int,input().split(" ")))

for i in range(1, n):
    j = i-1
    value = number[i]
    while number[j] > value and j >= 0:
        number[j+1] = number[j]
        j -= 1
    number[j+1] = value

sum = 0
for i in range(n):
    for j in range(i+1):
        sum += number[j]
print(sum)
