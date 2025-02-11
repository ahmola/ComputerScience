# gpt도 아니고 내 꺼도, 블로그꺼도 계속 nzec오류가 뜨는데 그냥 문제에 하자가 있는 것 같다. 일단 답은 맞는 것 같다
l = int(input())

s = list(map(int, input().split()))
s.sort()

n = int(input())
result = 0

if n not in s :
    for i in range(s[0]+1, n+1) :
        for j in range(n, max(s[-1], n)+1) :
            is_s = True
            for k in s :
                if k in range(i, j+1) :
                    is_s = False
                    break
            if is_s and i != j:
                result += 1

print(result)
# 이건 gpt가 푼 거
# import sys

# # 입력 받기
# l = int(sys.stdin.readline().strip())
# s = list(map(int, sys.stdin.readline().split()))
# n = int(sys.stdin.readline().strip())

# # n이 이미 S에 있다면 좋은 구간을 만들 수 없음
# if n in s:
#     print(0)
#     sys.exit()

# # S를 정렬
# s.sort()

# # n보다 작은 가장 큰 수(low)와 n보다 큰 가장 작은 수(high) 찾기
# low, high = 0, float('inf')

# for x in s:
#     if x < n:
#         low = x
#     elif x > n:
#         high = x
#         break

# # 좋은 구간의 개수 계산
# count = (n - low) * (high - n) - 1
# print(count)