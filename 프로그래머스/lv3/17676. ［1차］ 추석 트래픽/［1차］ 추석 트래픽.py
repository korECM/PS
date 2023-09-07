import re
from collections import deque

p = re.compile('\d{4}-\d{2}-\d{2} (\d{2}):(\d{2}):(\d{2}).(\d{3}) ([\d.]+)s')


def convert(line: str):
    find = p.findall(line)[0]
    hour, minute, sec, ms = map(int, find[:-1])
    duration = float(find[-1])
    end_time = ms + 1000 * (sec + 60 * (minute + 60 * hour))
    return end_time, int(duration * 1000)


def solution(lines):
    answer = 0
    times = deque()
    for line in lines:
        end_time, duration = convert(line)
        times.append((end_time - duration + 1, end_time))

    start_time_based = deque(sorted(times, key=lambda x: x[0]))
    end_time_based = deque(sorted(times, key=lambda x: x[1]))
    count = 0
    while start_time_based and end_time_based:
        st, et = start_time_based[0], end_time_based[0]
        t = min(st[0], et[1])
        while start_time_based:
            if start_time_based[0][0] < t + 1000:
                count += 1
                start_time_based.popleft()
            else:
                break
        while end_time_based:
            if end_time_based[0][1] < t:
                count -= 1
                end_time_based.popleft()
            else:
                break
        answer = max(answer, count)
        if end_time_based and end_time_based[0][1] == t:
            count -= 1
            end_time_based.popleft()

    return answer


# 2016-09-15 03:10:33.020 0.011s

solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
