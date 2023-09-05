from typing import List

def solution(n:int, arr1:List[int], arr2:List[int]):
    answer = []
    for a, b in zip(arr1, arr2):
        line = []
        rest = a | b
        while rest:
            if rest % 2 == 1:
                line.append("#")
            else:
                line.append(" ")
            rest //= 2
        while len(line) < n:
            line.append(" ")
        answer.append("".join(reversed(line)))
    print(answer)
    return answer