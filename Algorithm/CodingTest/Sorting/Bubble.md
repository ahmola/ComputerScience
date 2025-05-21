# Bubble Sort

인접한 두 데이터를 비교하며 정렬한다.

가장 큰 수가 배열의 맨 끝으로 "거품처럼" 밀려나듯이 정렬한다.

구현이 간단하나 비효율적

## 시간 복잡도

- 최선 : O(N)

- 최악 : O(N^2)

- 평균 : O(N^2)

## Python Code

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1): # 전체 패스 횟수
            # 한 번의 패스에서 가장 큰 원소가 맨 뒤로 이동하므로,
            # 다음 패스에서는 마지막 원소를 제외하고 비교
            swapped = False # 최적화: 이미 정렬된 경우 불필요한 패스 중단
            for j in range(n - 1 - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] # swap
                    swapped = True
            if not swapped: # 한 번의 패스 동안 교환이 없었다면, 이미 정렬된 상태
                break
        return arr

    # 예시
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("버블 정렬 전:", arr)
    bubble_sort(arr)
    print("버블 정렬 후:", arr) # [11, 12, 22, 25, 34, 64, 90]