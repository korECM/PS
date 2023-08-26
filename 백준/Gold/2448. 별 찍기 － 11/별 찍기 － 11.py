import sys

class IO:
    @staticmethod
    def num() -> int: return int(sys.stdin.readline())
    
    @staticmethod
    def println(*args: any, sep: str = ' '): sys.stdout.write(sep.join(map(str, args)) + '\n')

N = IO.num()
graph = [[' '] * 2 * N for _ in range(N)]


def recursive(x: int, y: int, n: int):
    if n == 3:
        graph[y][x] = '*'
        graph[y + 1][x - 1] = graph[y + 1][x + 1] = "*"
        for i in range(-2, 3):
            graph[y + 2][x + i] = "*"
    else:
        n //= 2
        recursive(x, y, n)
        recursive(x - n, y + n, n)
        recursive(x + n, y + n, n)


recursive((2 * N) // 2 - 1, 0, N)
for g in graph:
    IO.println(''.join(g))
