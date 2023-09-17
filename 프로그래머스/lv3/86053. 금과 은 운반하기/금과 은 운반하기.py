def check(a,b,g,s,w,t, time):
    total, tg, ts = 0,0,0
    for gg,ss,ww,tt in zip(g,s,w,t):
        div = time // tt
        # 광물 전달 횟수
        count = div // 2 + div % 2
        tmp = min(ww * count, gg + ss)
        total += tmp
        tg += min(tmp, gg)
        ts += min(tmp, ss)
    return total >= a + b and tg >= a and ts >= b
        
        
def solution(a, b, g, s, w, t):
    start, end = 0, 4 * 10 ** 14
    # 최댓값 찾기
    # [start, end]
    while start < end:
        mid = (start + end) // 2
        if check(a, b, g, s, w, t, mid):
            end = mid
        else:
            start = mid + 1
    return start

