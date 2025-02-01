x = int(input(""))
 
# 2의 지수승이라면
if x & (x-1) == 0 :
    print(1)
else :
    result = [64]
    i = 0
    sum = 64

    # 막대가 하나만 있는데 반으로 쪼개도 x보다 클 때
    while True :
        result[i] = int(result[i] / 2)
        if result[i] < x :
            result.append(result[i])
            i += 1
            break
    
    # 막대가 2개 이상일 때
    while True :
        result[i] = int(result[i] / 2)

        sum = 0
        for r in result : sum += r

        # 막대 길이의 합이 작다면
        if sum < x:
            # 반으로 나눴던 막대를 하나 추가
            result.append(result[i])
            i += 1
        # 같아지면 루프 탈출
        elif sum == x:
            break
    
    # i는 인덱스이므로 1추가
    print(i+1)