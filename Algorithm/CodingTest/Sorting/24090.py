# 문제에서 짜라는데로 짯는데 에러가 뜨면 어쩌라는건지;;
def partition(arr, p, r):
    global count
    x = arr[r]
    i = p-1

    for j in range(p, r):
        if arr[j] <= x:
            count += 1
            i += 1
            if count == k:
                if arr[i] < arr[j] :
                    print(arr[i], arr[j])
                else:
                    print(arr[j], arr[i])
            arr[i], arr[j] = arr[j], arr[i]
    
    if i+1 != r:
        count += 1
        if count == k:
            if arr[i+1] < arr[r]: 
                print(arr[i+1], arr[r])
            else:
                print(arr[r], arr[i+1])
        arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)


n, k = map(int,input().split(" "))
number = list(map(int, input().split(" ")))
count = 0
quick_sort(number, 0, n-1)
if count < k :
    print(-1)