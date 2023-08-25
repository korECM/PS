import sys
                
R, C = map(int, sys.stdin.readline().split())
board = [[ord(a) - 65for a in sys.stdin.readline().rstrip()] for _ in range(R)]
alphabets = [False for _ in range(26)]
alphabets[board[0][0]] = True
answer, cnt = 0, 1
words = set()
for b in board:
    words.update(b)
words_count = len(words)

g_dx, g_dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x: int, y: int):
    global answer, cnt
    if answer == words_count:
        return answer

    for i in range(4):
        nx, ny = x + g_dx[i], y + g_dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            alphabet = board[ny][nx]
            if not alphabets[alphabet]:
                alphabets[alphabet] = True
                cnt += 1
                dfs(nx, ny)
                cnt -= 1
                alphabets[alphabet] = False
    if cnt > answer:
        answer = cnt


dfs(0, 0)

print(answer)
             