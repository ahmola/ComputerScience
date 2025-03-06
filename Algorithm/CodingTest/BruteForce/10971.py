from itertools import permutations

def travel(cost, n):
    min_cost = float('inf')

    city = list(range(1, n))

    for per in permutations(city, n-1):
        sum_cost = 0
        route = list(per)
        last_index = 0
        is_not_break = True

        for i in range(len(route)):
            if cost[last_index][route[i]] == 0 :
                is_not_break = False
                break
            sum_cost += cost[last_index][route[i]]
            last_index = route[i]

        if cost[last_index][0] != 0 and is_not_break:
            sum_cost += cost[last_index][0]
            min_cost = min(min_cost, sum_cost)
    
    return min_cost

n = int(input())
cost = [list(map(int, input().split(" "))) for _ in range(n)]

print(travel(cost, n))