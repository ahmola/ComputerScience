# 음수일 때 int()를 쓰면 값이 더 내려가는 경우가 발생함. //를 쓰면 몫만 반환하므로 //를 쓰는 것이 더 안전함
a, b = map(int, input().split())
if b-a > 0 :
    print((a+b) * (b-a+1) // 2)
else :
    print((a+b)*(a-b+1)//2)