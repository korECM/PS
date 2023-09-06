from sys import stdin as ssi


class IO:
    @staticmethod
    def input() -> str: return ssi.readline().rstrip()

    @staticmethod
    def nums(): return map(int, ssi.readline().split())


N, M = IO.nums()
true_set = set([*IO.nums()][1:])
parties = [set([*IO.nums()][1:]) for _ in range(M)]

if len(true_set) == 0:
    print(M)
else:
    for i in range(M):
        for party in parties:
            if party & true_set and (party - true_set):
                true_set.update(party)
                break
    count = 0
    for party in parties:
        if not (party & true_set):
            count += 1
    print(count)
