def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    for truck in truck_weights:
        while sum(bridge[1:]) + truck > weight:
            bridge.pop(0)
            bridge.append(0)
            time += 1
        bridge.pop(0)
        bridge.append(truck)
        time += 1

    last = 0
    left, right = 0, len(bridge)
    while left < right:
        does_found = False
        mid = (left + right) // 2
        for i in range(right - 1, mid-1, -1):
            if bridge[i] != 0:
                last = (i + 1)
                does_found = True
                break
        if does_found:
            break
        right = mid
    return time + last

print(solution(2, 10, [7,4,5,6]))