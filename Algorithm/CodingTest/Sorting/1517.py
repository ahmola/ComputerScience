# merger sort
# O(nlogn)
# 배열을 반으로 계속 나누고 마지막에는 항상 병합을 통해 left와 mid에서 각 요소를 비교하여 배열을 정리한다.
# 오른쪽 배열이 작아서 왼쪽 배열로 옮겨야될 경우에는 mid-i+1만큼 자리를 바꾸게 된다.
def merge(arr, left, right, mid):
    i,j= left, mid+1
    count = 0
    temp = []

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            count += (mid - i +1) # i번째 앞으로 이동시키면서 전부 swap한다고 가정
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= right:
        temp.append(arr[j])
        j += 1
    
    for k in range(len(temp)):
        arr[k+left] = temp[k]
    
    return count

def merge_sort(arr, left, right):
    if left >= right :
        return 0

    mid = (left+right)//2
    count = 0

    count += merge_sort(arr, left, mid)
    count += merge_sort(arr, mid+1, right)

    count += merge(arr, left, right, mid)

    return count
n = int(input())
number = list(map(int, input().split(" ")))
print(merge_sort(number, 0, n-1))