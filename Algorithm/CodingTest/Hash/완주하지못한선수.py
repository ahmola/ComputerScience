def solution(participant, completion):
    result = ""
    player = {}

    for par in participant:
        if par in player:
            player[par] += 1
        else:
            player[par] = 1

    for com in completion:
        if com in player:
            player[com] -= 1

    for p in player:
        if player[p]== 1:
            result = p
            break

    return result

print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))