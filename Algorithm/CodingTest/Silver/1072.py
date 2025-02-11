# 범위가 1억까지 주어졌고 변하는지만 체크하면 되므로 이진 탐색을 사용한다
x, y = map(int, input().split())

win_rate = y*100//x

# 승률이 99퍼 이상이면 변하지 않음
if win_rate >= 99 :
    print(-1)
else :
    left, right = 1, 100000000
    count = -1

    while left <= right :
        mid = (left+right) // 2
        new_rate = (y+mid)*100 // (x+mid)

        if new_rate > win_rate :
            count = mid
            right = mid - 1
        else :
            left = mid + 1

    print(count)