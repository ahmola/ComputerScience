# from itertools import permutations, product

# def simulteneous(first, second):
#     for solution in product(range(-999, 999), 2):
#         for per in permutations(solution):
#             per = list(per)
#             if first[0]*per[0] + first[1]*per[1] == first[2] and second[0]*per[0] + second[1]*per[1] == second[2]:
#                 return per

# equation = list(map(int, input().split(" ")))
# first = [equation[0], equation[1], equation[2]]
# second = [equation[3], equation[4], equation[5]]
# print(*simulteneous(first, second))

a,b,c,d,e,f = map(int, input().split(" "))

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f :
            print(x, y)