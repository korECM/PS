from sys import stdin as ssi


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


R, C, T = map(int, ssi.readline().split())
board = [[*map(int, ssi.readline().split())] for _ in range(R)]
air_purifiers = []
for i in range(R):
    if board[i][0] == -1:
        air_purifiers.append(i)

adjustment = [[0 for _ in range(C)] for _ in range(R)]
g_dx, g_dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(T):
    new_pos = set()
    for dy in range(R):
        for dx in range(C):
            if board[dy][dx] <= 0:
                continue
            spread_amount = board[dy][dx] // 5
            if spread_amount > 0:
                for i in range(4):
                    nx, ny = dx + g_dx[i], dy + g_dy[i]
                    if 0 <= nx < C and 0 <= ny < R:
                        if nx == 0 and ny in air_purifiers:
                            continue
                        adjustment[ny][nx] += spread_amount
                        adjustment[dy][dx] -= spread_amount
                        new_pos.add((nx, ny))
                        new_pos.add((dx, dy))

    for ax, ay in new_pos:
        board[ay][ax] += adjustment[ay][ax]
        adjustment[ay][ax] = 0

    for y in range(air_purifiers[0] - 1, -1, -1):
        board[y + 1][0] = board[y][0]

    board[0][0:-1] = board[0][1:]

    for y in range(0, air_purifiers[0]):
        board[y][C - 1] = board[y + 1][C - 1]

    board[air_purifiers[0]][2:] = board[air_purifiers[0]][1:-1]
    ###
    for y in range(air_purifiers[1], R - 1):
        board[y][0] = board[y + 1][0]

    board[-1][0:-1] = board[-1][1:]

    for y in range(R - 1, air_purifiers[1], -1):
        board[y][C - 1] = board[y - 1][C - 1]
    board[air_purifiers[1]][2:] = board[air_purifiers[1]][1:-1]

    board[air_purifiers[0]][0] = -1
    board[air_purifiers[0]][1] = 0
    board[air_purifiers[1]][0] = -1
    board[air_purifiers[1]][1] = 0

print(sum([sum(b) for b in board]) + 2)
