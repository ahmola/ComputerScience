import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operation = operation.split(" ")
        if operation[0] == "I":
            heapq.heappush(heap, int(operation[1]))
        else:
            if not heap:
                continue
            if operation[1] == "1":
                # 음수로 만들어서
                for i in range(len(heap)):
                    heap[i] = -heap[i]
                heapq.heapify(heap)
                # 음수에서 최솟값으로 만들어서 지움
                heapq.heappop(heap)
                # 다시 복구
                for i in range(len(heap)):
                    heap[i] = -heap[i]
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)
    if not heap:
        return [0, 0]
    return [max(heap), min(heap)]