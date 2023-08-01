import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
result = [0] * n
for i in range(n):
    result[i] = num_input()

output = []
stack_counter = 1
stack = []
for r in result:
    for _ in range(stack_counter, r + 1):
        stack.append(stack_counter)
        stack_counter += 1
        output.append("+")
    if stack_counter >= r:
        if not stack or stack.pop() != r:
            output = ["NO"]
            break
        else:
            output.append("-")
print(*output, sep='\n')
