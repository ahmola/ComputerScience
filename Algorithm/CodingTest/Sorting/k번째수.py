def solution(array, commands):
    answer = []

    for com in commands:
        i, j, k = com[0] - 1, com[1] - 1, com[2] - 1
        numbers = array[i:j + 1]
        numbers.sort()
        answer.append(numbers[k])

    return answer
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))