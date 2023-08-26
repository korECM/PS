import sys

s = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
stack = []
for c in s:
    stack.append(c)
    while len(stack) >= len(pattern) and all([stack[~i] == pattern[~i] for i in range(len(pattern))]):
        for i in range(len(pattern)):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')

