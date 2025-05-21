# Selection Sort

배열에서 가장 작은 수를 찾아서 맨 앞(또는 뒤)의 원소와 교환하는 과정을 반복함

비효율적이지만, swap횟수가 버블 정렬보다 적다.

## 시간 복잡도

- 최선 : O(N^2)

- 최악 : O(N^2)

- 평균 : O(N^2)

## Python Code

    def selection_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            min_idx = i # 현재 정렬되지 않은 부분에서 가장 작은 원소의 인덱스
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            # 가장 작은 원소를 찾았으면 현재 위치의 원소와 교환
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    # 예시
    arr = [64, 25, 12, 22, 11]
    print("선택 정렬 전:", arr)
    selection_sort(arr)
    print("선택 정렬 후:", arr) # [11, 12, 22, 25, 64]