import sys

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

def generate_p(n: int):
    return ''.join(['I' if i % 2 == 0 else 'O' for i in range(n * 2 + 1)])


n, m = num_input(), num_input()
s = input()
p = generate_p(n)
p_length = (n * 2 + 1)
count = 0
for i in range(0, m - p_length + 1):
    if s[i:i + p_length] == p:
        count += 1
print(count)
