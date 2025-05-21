# Heap Sort

Heap 자료구조를 사용하여 정렬한다.

Heap 완전 이진 트리 형태로 부모 노드가 자식노드보다 크거나(최대힙) 작아야한다(최소힙).

Heap은 배열에서 0 ~ n//2 - 1까지 비 리프 노드들이다.

또한 자식 노드들은 왼쪽은 index*2 + 1, 오른쪽은 index*2 + 2로 설정한다.

그러므로 리프노드의 시작 인덱스는 항상 n//2가 된다.

1. 주어진 배열로 최대 힙을 만든다.

2. 가장 큰 값을 배열의 마지막 요소와 교환하고 크기를 1 줄임

3. 줄어든 힙을 다시 재구성(heapify)

4. 힙의 크기가 1이 될 때까지 반복

Python에서 Heap은 기본적으로 최대힙이다.

항상 똑같은 시간 복잡도를 가진다.

## 시간 복잡도

- 항상 O(NlogN)

## Python Code

    def heapify(arr, n, i):
        largest = i  # 부모 노드를 가장 큰 값으로 초기화
        left = 2 * i + 1 # 왼쪽 자식
        right = 2 * i + 2 # 오른쪽 자식

        # 왼쪽 자식이 존재하고, 부모보다 크다면 largest 업데이트
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 오른쪽 자식이 존재하고, 현재 largest보다 크다면 largest 업데이트
        if right < n and arr[right] > arr[largest]:
            largest = right

        # largest가 부모가 아니라면 (즉, 자식 중 더 큰 값이 있다면) 교환하고 재귀적으로 heapify 호출
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)

        # 1. 최대 힙 구축 (맨 뒤부터 거슬러 올라가며 heapify)
        # n//2 - 1 부터 0까지: 비-리프 노드들
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        # 2. 힙에서 원소를 하나씩 추출하여 정렬
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] # 현재 루트(가장 큰 값)를 배열의 마지막으로 이동
            heapify(arr, i, 0) # 줄어든 힙에 대해 다시 heapify

        return arr

    # 예시
    arr = [12, 11, 13, 5, 6, 7]
    print("힙 정렬 전:", arr)
    heap_sort(arr)
    print("힙 정렬 후:", arr) # [5, 6, 7, 11, 12, 13]