from typing import List
from collections import deque
    
# 40분
    
def str_to_min(s: str):
    hour, minute = map(int, s.split(":"))
    return hour * 60 + minute


def min_to_str(minute : int):
    hour = minute // 60
    minute %= 60
    h = str(hour) if hour >= 10 else f'0{hour}'
    m = str(minute) if minute >= 10 else f'0{minute}'
    return h + ":" + m

def solution(n : int, t : int, m: int, timetable):
    timetable = sorted([str_to_min(t) for t in timetable], reverse=True)
    shuttle_time = str_to_min("09:00")
    for i in range(n - 1):
        for _ in range(m):
            if timetable and timetable[-1] <= shuttle_time:
                timetable.pop()
        shuttle_time += t
    timetable = [i for i in timetable if i <= shuttle_time]
    while m > 1 and timetable:
        timetable.pop()
        m -= 1
    return min_to_str(timetable[-1] - 1 if timetable else shuttle_time)
