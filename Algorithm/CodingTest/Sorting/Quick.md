# Quick Sort

분할 정복 방식을 사용하는 정렬 기법

1. 배열에서 pivot을 하나 선택

2. pivot을 기준으로 배열을 세 개의 부분 배열로 분할

3. 분할된 배열 중, pivot보다 작은 배열과 큰 배열을 각각 재귀적으로 퀵 정렬 수행 후 병합

## 시간 복잡도

- 최선 : O(NlogN)

- 최악 : O(NlogN)

- 평균 : O(N^2)

## Python Code

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2] # 중간 값을 피벗으로 선택 (다양한 피벗 선택 전략 가능)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        
        return quick_sort(less) + equal + quick_sort(greater)

    # 예시
    arr = [10, 7, 8, 9, 1, 5]
    print("퀵 정렬 전:", arr)
    sorted_arr = quick_sort(arr)
    print("퀵 정렬 후:", sorted_arr) # [1, 5, 7, 8, 9, 10]