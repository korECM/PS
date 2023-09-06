from sys import stdin as ssi


class IO:
    @staticmethod
    def nums(): return map(int, ssi.readline().split())


N, M = IO.nums()
truth = [*IO.nums()][1:]
parties = [[*IO.nums()][1:] for _ in range(M)]


def find(x: int):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a: int, b: int):
    pa, pb = find(a), find(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


if len(truth) == 0:
    print(M)
else:
    KNOWN_TRUTH = 0
    parent = [i for i in range(N + 1)]
    for person in truth:
        parent[person] = KNOWN_TRUTH

    for party in parties:
        for i in range(len(party) - 1):
            union(party[i], party[i + 1])

    count = 0
    for party in parties:
        if not any([find(person) == KNOWN_TRUTH for person in party]):
            count += 1
    print(count)
