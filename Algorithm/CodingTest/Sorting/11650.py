# quick sort
# W(n^2), O(nlogn)
# 하나의 피벗을 고른다.(대게 맨 오른쪽)
# 피벗보다 작은 경우 왼쪽, 같으면 중간, 크면 오른쪽 배열에 삽입하여 합친다.
def quick_sort(coor):
    if len(coor) <= 1:
        return coor
    pivot = coor[len(coor)//2]
    left = []
    right = []
    equal = []

    for p in range(len(coor)):
        if coor[p] < pivot:
            left.append(coor[p])
        elif coor[p] > pivot:
            right.append(coor[p])
        else:
            equal.append(coor[p])

    return quick_sort(left)+equal+quick_sort(right)

n = int(input())
coor = [list(map(int, input().split(" "))) for _ in range(n)]
coor = quick_sort(coor)

for c in coor : print(*c)