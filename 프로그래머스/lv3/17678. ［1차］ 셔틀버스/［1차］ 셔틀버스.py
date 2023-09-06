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
    # 마지막 셔틀버스 제외하고 크루 제거
    for i in range(n - 1):
        for _ in range(m):
            if timetable and timetable[-1] <= shuttle_time:
                timetable.pop()
        shuttle_time += t
    # 마지막 셔틀버스를 탈 수 없는 크루 제거
    timetable = [i for i in timetable if i <= shuttle_time]
    # 마지막 한 명 남을 때까지 크루 제거
    while m > 1 and timetable:
        timetable.pop()
        m -= 1
    # 마지막 한 명보다 1분 일찍 타기
    # 혹은 셔틀 시간 딱 맞춰서
    return min_to_str(timetable[-1] - 1 if timetable else shuttle_time)
