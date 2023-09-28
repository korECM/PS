data = [1, 1, 2, 2, 2, 8]
ip = map(int, input().split())
for a, b in zip(data, ip):
    print(a - b, end=' ')