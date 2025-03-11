from itertools import combinations


def distance(house, chick):
    sum = 0
    for h in house:
        min_distance = float("Inf")
        for c in chick:
            min_distance = min(min_distance, (abs(h[0]-c[0])+ abs(h[1]-c[1])))
        sum += min_distance
    return sum

def chicken(city, n, m):
    chicken_distance = float("Inf")
    # 치킨집 좌표
    store = [[i, j] for i in range(n) for j in range(n) if city[i][j] == 2]
    # 집
    house = [[i, j] for i in range(n) for j in range(n) if city[i][j] == 1]

    # 운영할 치킨집을 고름
    for i in range(1, m+1):
        for chick in combinations(store, i):
            chick = list(chick)
            chicken_distance = min(distance(house, chick), chicken_distance)
    
    return chicken_distance

n, m = map(int, input().split(" "))
city = [list(map(int, input().split(" "))) for _ in range(n)]

print(chicken(city, n, m))