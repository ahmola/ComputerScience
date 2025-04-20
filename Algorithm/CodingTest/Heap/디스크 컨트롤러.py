import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간 기준 정렬
    heap = []
    time = 0
    idx = 0
    total_time = 0
    count = 0

    while count < len(jobs):
        # 현재 시간까지 요청된 job들 heap에 추가
        while idx < len(jobs) and jobs[idx][0] <= time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if heap:
            work_time, request_time = heapq.heappop(heap)
            time += work_time
            total_time += (time - request_time)
            count += 1
        else:
            # 아직 작업이 없는 경우, 다음 요청 시간까지 점프
            time = jobs[idx][0]

    return total_time // len(jobs)