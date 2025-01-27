testcase = int(input(""))
result = []

if 1 <= testcase <= 100 :
    for i in range(testcase) :
        g, c, e = map(int, input().split())
        
        # 문제에 변수 범위를 줘놓고 범위를 걸면 틀렸다고 하는데 문제 오류 같음
        if 1 <= g <= 3 and 0 <= c <= 100 and 1 <= e <= 100 : 
            if c >= e:
                result.append(0)
            else:
                d = 0
                if g == 1 :
                    d = 1
                elif g == 2 :
                    d = 3
                elif g == 3 :
                    d = 5
                result.append((e - c) * d)
    
    for r in result :
        print(r)