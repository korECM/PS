from itertools import product


class Solution:

    def diffWaysToCompute(self, expression: str) -> list[int]:
        if expression.isdigit():
            return [int(expression)]
        answer = []
        for i in range(len(expression)):
            if expression[i] in "+-*/":
                for aa, bb in product(self.diffWaysToCompute(expression[:i]), self.diffWaysToCompute(expression[i + 1:])):
                    answer.append(eval(f'{aa}{expression[i]}{bb}'))
        return answer
