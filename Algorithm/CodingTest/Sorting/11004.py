def quick_sort(arr, k):
    j = len(arr)

    left = []
    equal = []
    right = []

    for p in range(j):
        if arr[p] < arr[j-1]:
            left.append(arr[p])
        elif arr[p] > arr[j-1]:
            right.append(arr[p])
        else:
            equal.append(arr[p])
    
    if k <= len(left):
        left.sort()
        print(left[k-1])
    elif k <= len(left)+len(equal):
        print(equal[0])
    else:
        right.sort()
        print(right[k-len(equal)-len(left)-1])
    

n, k = map(int, input().split(" "))
number = list(map(int, input().split(" ")))
quick_sort(number, k)