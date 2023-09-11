from itertools import permutations
from sys import stdin as ssi
from sys import stdout as sso

N, M = map(int, ssi.readline().split())

for result in permutations(range(1, N + 1), M):
    sso.write(' '.join(map(str, result)) + '\n')
