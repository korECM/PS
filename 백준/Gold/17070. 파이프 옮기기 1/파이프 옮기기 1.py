from sys import stdin as ssi

N = int(ssi.readline())
board = [[*map(int, ssi.readline().split())] for _ in range(N)]

if board[N - 1][N - 1] == 1:
    print(0)
else:
    dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
    # 0: 가로, 1 : 세로, 2 : 대각선
    dp[0][1][0] = 1
    for y in range(N):
        for x in range(N):
            for k in range(3):
                if dp[y][x][k] == 0:
                    continue
                right = x + 1 < N and not board[y][x + 1]
                down = y + 1 < N and not board[y + 1][x]
                diagonal = right and down and not board[y + 1][x + 1]

                if k == 0 and right:
                    dp[y][x + 1][0] += dp[y][x][k]
                    if diagonal:
                        dp[y + 1][x + 1][2] += dp[y][x][k]
                elif k == 1 and down:
                    dp[y + 1][x][1] += dp[y][x][k]
                    if diagonal:
                        dp[y + 1][x + 1][2] += dp[y][x][k]
                elif k == 2:
                    if right:
                        dp[y][x + 1][0] += dp[y][x][k]
                    if down:
                        dp[y + 1][x][1] += dp[y][x][k]
                    if diagonal:
                        dp[y + 1][x + 1][2] += dp[y][x][k]
    print(sum(dp[N - 1][N - 1]))
