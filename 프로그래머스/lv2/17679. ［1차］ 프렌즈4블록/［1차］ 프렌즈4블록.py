def get_pos(x, y):
    return (x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)


def check(x: int, y: int, board):
    start = board[y][x]
    if start == "팡":
        return False
    return all([start == board[ny][nx] for nx, ny in get_pos(x, y)])


def solution(m, n, board):
    board = [[c for c in b] for b in board]
    while True:
        target = set()
        for y in range(m - 1):
            for x in range(n - 1):
                if check(x, y, board):
                    target.update(get_pos(x, y))

        if not target:
            break

        for x, y in sorted(target, key=lambda t: (t[1], t[0])):
            for ny in range(y, -1, -1):
                board[ny][x] = board[ny - 1][x] if ny >= 1 else "팡"

    return sum([b.count("팡") for b in board])
