mem = {}


def get_combinations(n, cur, acc):
    if n == 0:
        acc.add(tuple(cur))
        return
    acc.add(tuple(cur + [n]))
    for i in range(1, n + 1):
        get_combinations(n - i, cur + [i], acc)


def solution(n):
    if n <= 2:
        return max(n, 1)

    if n not in mem:
        mem[n] = 0

        targets = set()
        get_combinations(n, [], targets)
        for target in targets:
            count = 1
            for element in target:
                count *= solution(element - 1)
            mem[n] += count
    
    return mem[n]
