n, m = map(int, input().split())
# 패키지 가격, 개별 줄 가격
price = [list(map(int, input().split())) for _ in range(m)]

# 6개를 묶음으로 살 때
six_price = []
# 개별로 살 때
one_price = []

for i in range(len(price)) :
    six_price.append(price[i][0])
    # 개별로 6개를 살 때
    six_price.append(price[i][1]*6)
    one_price.append(price[i][1])

# 정렬을 통해 첫 번째 요소가 최솟값이 되도록 함
six_price.sort()
one_price.sort()
six_price = six_price[0]
one_price = one_price[0]

least_price = 0

# 6개를 묶음으로 사는 경우와 낱개로 사는 경우를 나눔
sixgroup = n // 6
least_price += sixgroup*six_price
onegroup = n % 6
least_price += onegroup*one_price

# 낱개를 추가로 사는 것보다 묶음을 하나 더 사는게 적을 경우
if six_price*(sixgroup+1) < least_price :
    print(six_price*(sixgroup+1))
else :
    print(least_price)