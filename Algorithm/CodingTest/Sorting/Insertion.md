# Insertion Sort

원소 앞의 정렬된 부분 배열의 알맞은 위치에 끼워넣는 방식

카드를 뒤로 옮겨서 올바른 위치 사이에 끼워넣는 방식을 말한다.

데이터 양이 적거나, 거의 정렬되었을 때 효과적

## 시간 복잡도

- 최선 : O(N)

- 최악 : O(N^2)

- 평균 : O(N^2)

## Python Code

    def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n): # 두 번째 원소부터 시작 (첫 번째 원소는 이미 정렬된 것으로 간주)
            key = arr[i] # 현재 삽입할 원소
            j = i - 1    # key가 삽입될 위치를 찾기 위해 비교할 인덱스

            # key보다 큰 원소들은 한 칸씩 뒤로 밀어냄
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key # key를 올바른 위치에 삽입
        return arr

    # 예시
    arr = [12, 11, 13, 5, 6]
    print("삽입 정렬 전:", arr)
    insertion_sort(arr)
    print("삽입 정렬 후:", arr) # [5, 6, 11, 12, 13]