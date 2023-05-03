dx = [0, 1, -1]
dy = [1, 0, -1]

def solution(n):
    angle = -1
    cnt = 1
    x, y = 0, -1
    answer = []
    array = [[0] * (i + 1) for i in range(n )]
    
    for i in range(n, 0, -1):
        angle = (angle + 1) % 3
        for _ in range(i):
            y += dy[angle]
            x += dx[angle]
            array[y][x] = cnt
            cnt += 1
    return [i for j in array for i in j]