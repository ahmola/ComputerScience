# Merge Sort

분할 정복 방식을 사용하는 정렬 기법

1. 배열을 절반으로 재귀적으로 1개가 남을 때까지 분할

2. 분할된 부분 배열을 정렬과 동시에 병합

시간 복잡도가 일정하다

## 시간 복잡도

- 최선, 최악, 평균 모두 O(NlogN)

## Python Code

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 재귀적으로 분할
        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)

        # 병합
        return merge(left_sorted, right_sorted)

    def merge(left, right):
        merged_arr = []
        i = j = 0

        # 양쪽 배열을 비교하여 작은 원소부터 merged_arr에 추가
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged_arr.append(left[i])
                i += 1
            else:
                merged_arr.append(right[j])
                j += 1
        
        # 남은 원소들 추가
        while i < len(left):
            merged_arr.append(left[i])
            i += 1
        while j < len(right):
            merged_arr.append(right[j])
            j += 1
            
        return merged_arr

    # 예시
    arr = [11, 10, 8, 9, 5, 7, 1]
    print("병합 정렬 전:", arr)
    sorted_arr = merge_sort(arr)
    print("병합 정렬 후:", sorted_arr) # [1, 5, 7, 8, 9, 10, 11]