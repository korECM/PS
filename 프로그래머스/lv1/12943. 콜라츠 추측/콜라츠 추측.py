def solution(num):
    return s(num, 0)

def s(num, t):
    if t > 500:
        return -1
    if num == 1:
        return t
    if num % 2 == 0:
        return s(num // 2, t + 1)
    else:
        return s(num * 3 + 1, t + 1)