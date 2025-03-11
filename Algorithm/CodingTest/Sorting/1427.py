# 선택 정렬
# 리스트 내에서 가장 작은 원소를 찾는다
# 가장 작은 원소를 맨 앞의 원소와 교체한다
# 맨 앞의 원소를 제외하고 다음 원소부터 위 과정을 반복한다.
number = input()
number = [int(n) for n in number]

for i in range(len(number)-1):
    index = i
    for j in range(i, len(number)):
        if number[index] < number[j]:
            index = j
    number[i], number[index] = number[index], number[i]

for n in number:
    print(n, end="")
print()