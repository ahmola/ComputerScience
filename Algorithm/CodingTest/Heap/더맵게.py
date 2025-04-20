import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) > 1 and any(food < K for food in scoville):
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        heapq.heappush(scoville, one + two * 2)
        count += 1

    if scoville[0] < K:
        return -1
    return count