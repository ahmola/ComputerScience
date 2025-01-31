# 평균 시도가 많은 문제들은 건드리지 않는게 좋은 것 같다. 괜히 사람들이 많이 시도한게 아니다;; 하나씩 하자가 있다

n = int(input(""))
m = list(map(int, input()))
if len(m) == n :
    k = int(input(""))
    result = True

    index = 0
    while m[index] != 1 and index < n: index += 1

    if index == n:
        result = False
        print("NO")
    else:
        m = m[index:]
        n = len(m)

        if k > n:
            result = False
            print("NO")
        else:
            for i in range(n-1, n-k-1, -1):
                if m[i] == 1:
                    if i == 0:
                        break
                    result = False
                    print("NO")
                    break

        if result:
            print("YES")