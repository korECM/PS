def solution(n):
    return s(n, 1, 3)


def s(n, f, t):
    if n == 1:
        return [[f, t]]

    if {f, t} == {1, 2}:
        m = 3
    elif {f, t} == {1, 3}:
        m = 2
    elif {f, t} == {2, 3}:
        m = 1

    return s(n - 1, f, m) + [[f, t]] + s(n - 1, m, t)
