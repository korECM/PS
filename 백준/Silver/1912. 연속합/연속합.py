import sys
from sys import stdin as ssi

N = int(ssi.readline())
data = [*map(int, ssi.readline().split())]
for i in range(1, N):
    data[i] += data[i - 1]
min_v, answer = sys.maxsize, data[0]
for a in data:
    answer = max(answer, a, a - min_v)
    min_v = min(min_v, a)
print(answer)
