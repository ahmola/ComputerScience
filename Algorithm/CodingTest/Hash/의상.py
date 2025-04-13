def solution(clothes):
    # 초기화할 때 아무것도 선택하지 않는 경우의 수 포함
    closet = {item[1] : 1 for item in clothes}
    for c in clothes:
        closet[c[1]] += 1

    answer = 1
    for value in closet.values():
        answer *= value

    # 마지막으로 모두 다 선택하지 않는 한 가지 경우는 제외
    return answer-1

print(solution([["yellow_hat", "headgear"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"]]))