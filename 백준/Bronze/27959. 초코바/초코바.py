from sys import stdin as ssi

a, b = map(int, ssi.readline().split())
print("Yes" if a * 100 >= b else "No")
