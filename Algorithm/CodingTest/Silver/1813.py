# 답지인데 솔직히 난 아직도 문제가 뭔지 모르겠다.
N = int(input())  # 항승이가 한 말의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트

# 가능한 참인 문장의 개수를 구하는 함수
def check_trues(truth_count):
    # truth_count가 참인 문장의 개수일 때, 그 상태가 가능한지 판단
    true_statements = 0
    for num in numbers:
        if num == truth_count:
            true_statements += 1
    return true_statements

max_true = -1  # 참인 문장의 최대 개수
for i in range(N + 1):
    if check_trues(i) == i:
        max_true = max(max_true, i)

print(max_true)