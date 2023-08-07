import re
import sys

def input() -> str:
    return sys.stdin.readline().rstrip()

split_input = re.split('(\\d+)', input())[1:-1]
operands, operators = list(map(int, split_input[::2])), split_input[1::2]

sum = operands[0]
temp_sum = 0
for op, operand in zip(operators, operands[1:]):
    if op == "+":
        if temp_sum:
            temp_sum += operand
        else:
            sum += operand
    else:
        temp_sum += operand
print(sum - temp_sum)
