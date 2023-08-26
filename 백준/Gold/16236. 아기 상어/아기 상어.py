import sys
from collections import defaultdict, deque

MAX = sys.maxsize


class IO:
    @staticmethod
    def input() -> str: return sys.stdin.readline().rstrip()

    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

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

N = IO.num()
board: list[list[int]] = [[*IO.nums()] for _ in range(N)]
fish_map: dict[int, list[tuple[int, int]]] = defaultdict(list)
sx, sy = 0, 0
size = 2
fish_eaten = 0

for y in range(N):
    for x in range(N):
        if board[y][x] == 9:
            sx, sy = x, y
            board[y][x] = 0
        elif board[y][x] > 0:
            fish_map[board[y][x]].append((x, y))


def get_time(targets: set[tuple[int, int]]) -> tuple[int, dict[tuple[int, int], int]]:
    queue = deque([(sx, sy, 0)])
    visited = {(sx, sy)}
    answer = {}
    min_time = MAX

    if not targets:
        return min_time, answer

    while queue:
        cx, cy, time = queue.popleft()
        if time > min_time:
            continue

        if (cx, cy) in targets:
            if time <= min_time:
                min_time = time
                answer[(cx, cy)] = time

        for nx, ny in Move.generate_hv(cx, cy, 0, N, 0, N):
            if (nx, ny) not in visited and board[ny][nx] <= size:
                visited.add((nx, ny))
                queue.append((nx, ny, time + 1))

    return min_time, answer


def get_target_candidates() -> list[tuple[int, int]]:
    return [item for i in range(1, size) if fish_map[i] for item in fish_map[i]]


def get_target() -> tuple[int, tuple[int, int]]:
    candidates = get_target_candidates()
    min_time, target_time_map = get_time(set(candidates))
    if min_time == MAX:
        return None, None
    min_target = sorted([p for p, t in target_time_map.items() if t == min_time], key=lambda p: (p[1], p[0]))[0]
    return min_time, min_target


time = 0

while True:
    add_time, target = get_target()
    if not target:
        break
    time += add_time

    fish_map[board[target[1]][target[0]]].remove(target)
    board[target[1]][target[0]] = 0
    sx, sy = target

    fish_eaten += 1
    if size == fish_eaten:
        fish_eaten = 0
        size += 1

print(time)

