# 오차 어쩌구하는 문제 중에는 정상이 없다
def max_cube_size(N, L, W, H):
    low, high = 1, min(L, W, H)
    
    # 절대 오차 10^-9 까지 허용하므로 작은 값까지 이분 탐색 수행
    while high - low >= 0:
        mid = (low + high) / 2
        
        # mid 크기의 정육면체를 넣을 수 있는 개수
        count = (L // mid) * (W // mid) * (H // mid)
        
        if count >= N:  # 가능하면 크기를 늘림
            low = mid + 0.00000001
        else:  # 불가능하면 크기를 줄임
            high = mid - 0.00000001

    return low

N, L, W, H = map(int, input().split())

print(f"{max_cube_size(N, L, W, H)}")