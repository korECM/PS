dx, dy = [1, 0, 0, -1], [0, 1, -1 , 0]

def get_pos(x,y):
    return ((x, y), (x+1,y), (x,y+1), (x +1, y+1))

def check(m: int, n : int, x: int, y : int, board):
    start = board[y][x]
    if start == "":
        return False
    if y == m - 1 or x == n - 1:
        return False
    target = get_pos(x,y)
    return all([board[y][x] == board[ny][nx] for nx,ny in target])
                
        

def solution(m, n, board):
    board = [[c for c in b] for b in board]
    answer = 0
    while True:
        target = set()
        for y in range(m - 1):
            for x in range(n - 1):
                if check(m,n,x,y,board):
                    for i in get_pos(x,y):
                        target.add(i)
        
        if not target:
            break
        answer += len(target)

        for x, y in sorted(target, key=lambda t : (t[1], t[0])):
            for ny in range(y, -1, -1):
                board[ny][x] = board[ny-1][x] if ny >= 1 else ""
        
    return answer