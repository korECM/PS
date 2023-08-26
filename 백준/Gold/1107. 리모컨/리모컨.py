min_value = 0


def solve(n: int, data: set[int], acc: str):
    global min_value
    if len(acc) > 6:
        return
    if acc:
        new_val = abs(n - int(acc)) + len(acc)
        if min_value > new_val:
            min_value = new_val
    for datum in data:
        solve(n, data, acc + str(datum))


def solve2():
    global min_value
    n, m = int(input()), int(input())
    min_value = abs(n - 100)

    if m == 10:
        print(abs(n - 100))
    elif m == 0:
        print(min(abs(n - 100), len(str(n))))
    else:
        solve(n, set(range(0, 10)) - set(map(int, input().split())), "")
        print(min_value)


solve2()
