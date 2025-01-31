# 퀵, 머지, 버블, 카운팅 하는 것도 죄다 안되면 어쩌라는건지 모르겠다
import time

s = time.time()

count = [0] * 10001

n = int(input())

for _ in range(n) :
    num = int(input())
    count[num] += 1

for i in range(1, 10001) :
    if count[i] != 0 :
        for _ in range(count[i]):
            print(i)

e = time.time()
print(f"{e-s}")