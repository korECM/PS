from sys import stdin as ssi

class IO:
    @staticmethod
    def nums(): return map(int, ssi.readline().split())

N, K = map(int, ssi.readline().split())
cargo = [[*map(int, ssi.readline().split())] for _ in range(N)]
pack = []
for i in range(N + 1):
    pack.append([])
    for c in range(K + 1):
        if i == 0 or c == 0:
            pack[i].append(0)
        else:
            weight, value = cargo[i - 1]
            if weight <= c:
                pack[i].append(max(pack[i - 1][c], value + pack[i - 1][c - weight]))
            else:
                pack[i].append(pack[i - 1][c])
print(pack[N][K])
