n, m = map(int, input().split())
if 1 <= m <= n <= 10**1000:
    print(n//m)
    print(n%m)