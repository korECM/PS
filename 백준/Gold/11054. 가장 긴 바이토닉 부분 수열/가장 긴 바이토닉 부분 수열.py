import sys

MAX = sys.maxsize


class IO:
    @staticmethod
    def num() -> int: return int(sys.stdin.readline())

    @staticmethod
    def nums(): return map(int, sys.stdin.readline().split())

N = IO.num()
data = [0] + [*IO.nums()]
dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i):
        if data[i] > data[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(N, 0, -1):
    for j in range(N, i, -1):
        if data[i] > data[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, dp1[i] + dp2[i])

print(answer)
