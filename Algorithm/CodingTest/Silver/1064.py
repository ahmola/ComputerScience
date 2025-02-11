# 예제가 좀 이상하다. 분명 마지막 예제는 평행사변형을 만들 수 잇는데 없다니...
import math

# 평행사변형은 두 변만 알면 된다. 세 점이 주어졌으므로 굳이 점d를 알아낼 필요는 없다. 세 점 중 2개를 선택해서 변으로 만들면 나머지는 자동 결정된다.
parall = list(map(int, input().split()))

# 세 점이 한 선에 위치하면 안됨. 근데 이거는 좀 복잡해서 나중에 따로 수정이 필요할 것 같다.
if parall[0] == parall[2] == parall[4] or parall[1] == parall[3] == parall[5] :
    print(-1.0)
else :
    # 즉, 계산을 세 번만 하면 됨
    sides = []

    for i in range(0, 3, 2) :
        for j in range(i+2, 5, 2) :
            sides.append(math.sqrt(pow(parall[i]-parall[j],2)+pow(parall[i+1]-parall[j+1],2)))

    sides.sort()
    print(sides)
    print((sides[2]+sides[1])*2 - (sides[0]+sides[1])*2)