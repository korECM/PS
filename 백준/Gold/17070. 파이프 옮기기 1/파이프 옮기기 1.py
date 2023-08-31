from sys import stdin as ssi

N = int(ssi.readline())
board = [[*map(int, ssi.readline().split())] for _ in range(N)]


def dfs(x1: int, y1: int, x2: int, y2: int):
    if x2 == N - 1 and y2 == N - 1:
        return 1

    result = 0
    right = x2 + 1 < N and not board[y2][x2 + 1]
    down = y2 + 1 < N and not board[y2 + 1][x2]
    diagonal = right and down and not board[y2 + 1][x2 + 1]

    # 가로
    if y1 == y2 and x2 - x1 == 1 and right:
        # 가로 밀기
        result += dfs(x1 + 1, y1, x2 + 1, y2)
        # 가로 밀면서 대각 회전
        if diagonal:
            result += dfs(x1 + 1, y1, x2 + 1, y2 + 1)
    # 세로
    elif x1 == x2 and y2 - y1 == 1 and down:
        # 세로 밀기
        result += dfs(x1, y1 + 1, x2, y2 + 1)
        # 세로 밀면서 대각 회전
        if diagonal:
            result += dfs(x1, y1 + 1, x2 + 1, y2 + 1)
    # 대각
    elif x1 + 1 == x2 and y1 + 1 == y2:
        # 가로
        if right:
            result += dfs(x1 + 1, y1 + 1, x2 + 1, y2)
        # 세로
        if down:
            result += dfs(x1 + 1, y1 + 1, x2, y2 + 1)
        # 대각
        if diagonal:
            result += dfs(x1 + 1, y1 + 1, x2 + 1, y2 + 1)
    return result


if board[N - 1][N - 1] == 1:
    print(0)
else:
    print(dfs(0, 0, 1, 0))
