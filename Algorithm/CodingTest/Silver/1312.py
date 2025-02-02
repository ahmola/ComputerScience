# 그냥 나누기 연산을 하면 이진법으로 인해 오류가 날 수 있다. 그러므로 직접 나머지에 10을 곱하고 다시 나눠 몫과 나머지를 구해야한다. 이 때 몫은 소수점 숫자를 나타내게 된다.
a,b,n = map(int, input().split())
r = a%b
digit = 0
for _ in range(n) :
    r *= 10
    digit = r // b
    r = r % b
print(digit)