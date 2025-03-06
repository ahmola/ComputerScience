from itertools import combinations, permutations

def operator(numbers, op):
    result = 0

    if op[0] == "+":
        result = numbers[0] + numbers[1]
    elif op[0] == "-":
        result = numbers[0] - numbers[1]
    elif op[0] == "*":
        result = numbers[0]*numbers[1]
    elif op[0] == "//":
        result = numbers[0]//numbers[1]

    index = 1
    for i in range(2, len(numbers)):
        if op[index] == "+":
            result += numbers[i]
        elif op[index] == "-":
            result -= numbers[i]
        elif op[index] == "*":
            result *= numbers[i]
        elif op[index] == "//":
            if result < 0:
                result = -(abs(result)//numbers[i])
            else:
                result = result//numbers[i]
        index += 1

    return result

n = int(input())
numbers = list(map(int,input().split(" ")))
# 0과 1로 이루어져있고, 순서대로 + - * //
o = list(map(int, input().split(" ")))
oper = []
for _ in range(o[0]): oper.append("+")
for _ in range(o[1]): oper.append("-")
for _ in range(o[2]): oper.append("*")
for _ in range(o[3]): oper.append("//")

min_value = None
max_value = None
for comb in combinations(oper, n-1):
    for per in permutations(comb):
        result = operator(numbers, per)
        if min_value == None or min_value > result:
            min_value = result
        if max_value == None or max_value < result:
            max_value = result
print(max_value)
print(min_value)