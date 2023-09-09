def check(n, times, check_time):
    return sum([check_time // t for t in times]) >= n

def solution(n, times):
    answer = 0
    times.sort()
    # 최소 구하기
    # [start, end]
    low, high = times[0] * (n // len(times)), times[-1] * (n // len(times) + 1)
    while low < high:
        mid = (low + high) // 2
        if check(n, times, mid):
            high = mid
        else:
            low = mid + 1
    return low