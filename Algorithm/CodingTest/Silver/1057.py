# 토너먼트에서 이기면 팀 번호를 다시 부여하는데 이 때 왼쪽으로 이동시킨다고 추상화하면됨. 이겨서 올라갈 때마다 팀 번호의 수가 줄어들어야함  
# 한 라운드가 끝날 때마다 팀 번호의 수가 절반이 줄어든다. 즉, 팀 번호에서 1을 더하고 2로 나눈 몫이 다음 팀 번호가 된다.
def tournament(a, b):
    round = 1  # 첫 번째 라운드부터 시작
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        if a == b:
            return round
        round += 1  # 라운드 증가
    return round

n, a, b = map(int, input().split())

print(tournament(a, b))