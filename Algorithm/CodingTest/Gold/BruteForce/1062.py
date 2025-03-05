from itertools import combinations

def count_readable(words, learned):
    count = 0
    for word in words:
        if word.issubset(learned):  # 배운 글자 안에 단어 글자가 모두 포함되면
            count += 1
    return count

def teaching(words, k):
    if k < 0:  # K가 5보다 작으면 아무 단어도 못 읽음
        return 0

    chars = set().union(*words)  # 모든 등장 글자 모으기
    if len(chars) <= k:
        return len(words)  # 모든 단어를 읽을 수 있음

    max_count = 0
    for comb in combinations(chars, k):  # 가능한 모든 글자 조합 탐색
        learned = {'a', 'n', 't', 'i', 'c'} | set(comb)
        # 만든 조합으로 모든 단어에서 검사하여 가장 많이 단어에 사용되는 조합에서의 횟수를 구한다.
        max_count = max(max_count, count_readable(words, learned))
    
    return max_count

# 입력
n, k = map(int, input().split())
k -= 5  # "antic"를 제외한 글자만 선택 가능

words = [set(input().strip('antic')) for _ in range(n)]  # 필요 없는 글자 제거
print(teaching(words, k))