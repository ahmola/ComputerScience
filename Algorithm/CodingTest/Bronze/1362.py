# 내가 짠 코드도 그렇고 gpt가 짠 코드도 계속 런타임에러내는데 왜인지 모르겠다

result = []

while True :
    o, w = map(int, input().split())
    if o == 0 and w == 0 :
        break

    is_dead = False
    while True :
        inter, n = input().split()
        n = int(n)
        if inter == "#" and n == 0 :
            if o/2 < w < o*2 :
                result.append("-)")
            elif o <= 0 :
                result.append("RIP")
            else :
                result.append("-(")
            break

        if inter == "F" and not is_dead :
            w += n
        elif inter == "E" and not is_dead:
            w -= n
        
        if w <= 0 :
            is_dead = True

for i, r in enumerate(result) : 
    print(f"{i+1} :{r}")