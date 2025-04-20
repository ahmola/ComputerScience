def solution(answers):
    who = []

    supo = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            supo[0] += 1
        if answers[i] == two[i % 8]:
            supo[1] += 1
        if answers[i] == three[i % 10]:
            supo[2] += 1

    max_value = max(supo)
    for i in range(3):
        if supo[i] == max_value:
            who.append(i + 1)
    return who