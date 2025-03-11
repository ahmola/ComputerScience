# 버블 정렬
# 원소와 그 앞의 원소를 비교하며 자리를 바꾸는 것을 반복한다.
# O(n^2)
n = int(input())
number = [int(input()) for _ in range(n)]

for _ in range(n-1):
    for j in range(n-1):
        if number[j] > number[j+1]:
            number[j], number[j+1] = number[j+1], number[j]

for num in number:
    print(num)