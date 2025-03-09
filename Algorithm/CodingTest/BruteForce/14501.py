from itertools import combinations

def day_check(day, indexes, n):
    current_day = 0

    for ind in indexes:
        if ind + day[ind] <= n and current_day <= ind+1:
            current_day = day[ind]+ind+1
        else:
            return False
    return True

def working(day, cost, n):
    result = 0

    for i in range(1, n+1):
        for indexes in combinations(range(n),i):
            max_cost = 0
            indexes = list(indexes)
            
            if day_check(day, indexes, n):
                for ind in indexes:
                    max_cost += cost[ind]
                result = max(max_cost, result)
            
    return result

n = int(input())
total = [list(map(int, input().split(" "))) for _ in range(n)]
day = []
cost = []

for i in range(n):
    day.append(total[i][0])
    cost.append(total[i][1])

print(working(day, cost, n))