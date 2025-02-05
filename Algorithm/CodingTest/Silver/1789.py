# 가장 작은 수부터 더해나가면 최대로 계산
n = int(input())
sum = 0
number = []
# 구하려는 수와 가까워지기(또는 같거나) 직전까지만 더함
for i in range(1, n) :
    if sum + i >= n :
        break
    sum += i
    number.append(i)
# 만약 같지 않더만 차수를 추가함
if sum != n :
    number.append(n - sum)
# 최댓값 출력
print(max(number))