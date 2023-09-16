N = int(input())
path = []


def hanoi(n: int, s: int, m: int, end: int):
    global path
    if n == 1:
        path.append(f'{s} {end}')
        return 1
    return hanoi(n - 1, s, end, m) + hanoi(1, s, m, end) + hanoi(n - 1, m, s, end)


count = hanoi(N, 1, 2, 3)
print(count)
print(*path, sep='\n')
