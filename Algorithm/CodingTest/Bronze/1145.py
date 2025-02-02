# 유클리드 호제법(최대 공약수)
def gcd(a,b) :
    while b :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return (a*b) // gcd(a,b)

num = list(map(int, input().split()))
num.sort()

result = []

# 5 combination 3
for i in range(3) :
    for j in range(i+1, 4) :
        for k in range(j+1, 5) :
            number = [num[i], num[j], num[k]]
            r = number[0]
            for l in range(1, 3) :
                r = lcm(r, number[l])
            result.append(r)
# 4중이라 시간 초과뜰줄 알았는데 이게 되네;;

print(min(result))
