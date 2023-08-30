from collections import defaultdict
from sys import stdin as ssi


class IO:
    @staticmethod
    def nums(): return map(int, ssi.readline().split())


class Move:
    @staticmethod
    def generate_hv(x: int, y: int, x_low: int, x_high: int, y_low: int, y_high: int):
        """
        상하좌우 이동
        """
        g_dx, g_dy = [1, -1, 0, 0], [0, 0, 1, -1]
        for g_i in range(len(g_dx)):
            g_cx, g_cy = x + g_dx[g_i], y + g_dy[g_i]
            if x_low <= g_cx < x_high and y_low <= g_cy < y_high:
                yield g_cx, g_cy


R, C, T = IO.nums()
board = [[0] for _ in range(R)]
air_purifiers = []
dust = set()
for i in range(R):
    board[i] = [*IO.nums()]
    if board[i][0] == -1:
        air_purifiers.append(i)

for _ in range(T):
    adjustment = defaultdict(int)
    for dy in range(R):
        for dx in range(C):
            if board[dy][dx] <= 0:
                continue
            spread_amount = board[dy][dx] // 5
            if spread_amount > 0:
                for nx, ny in Move.generate_hv(dx, dy, 0, C, 0, R):
                    if nx == 0 and ny in air_purifiers:
                        continue
                    adjustment[(nx, ny)] += spread_amount
                    adjustment[(dx, dy)] -= spread_amount
    for k, amount in adjustment.items():
        ax, ay = k
        board[ay][ax] += amount

    for y in range(air_purifiers[0] - 1, -1, -1):
        board[y + 1][0] = board[y][0]

    for x in range(1, C):
        board[0][x - 1] = board[0][x]

    for y in range(0, air_purifiers[0]):
        board[y][C - 1] = board[y + 1][C - 1]

    for x in range(C - 1, 1, -1):
        board[air_purifiers[0]][x] = board[air_purifiers[0]][x - 1]
    ###
    for y in range(air_purifiers[1], R - 1):
        board[y][0] = board[y + 1][0]

    for x in range(1, C):
        board[R - 1][x - 1] = board[R - 1][x]

    for y in range(R - 1, air_purifiers[1], -1):
        board[y][C - 1] = board[y - 1][C - 1]
    for x in range(C - 1, 1, -1):
        board[air_purifiers[1]][x] = board[air_purifiers[1]][x - 1]

    board[air_purifiers[0]][0] = -1
    board[air_purifiers[0]][1] = 0
    board[air_purifiers[1]][0] = -1
    board[air_purifiers[1]][1] = 0

print(sum([sum(b) for b in board]) + 2)
