import sys
from collections import Counter

def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())

s = input()
counter = Counter(s)
# 문자열이 짝수 길이이고 글자가 짝수 개가 아닌 경우
odd_count_list = list(filter(lambda x: x % 2 != 0, counter.values()))
if odd_count_list and len(s) % 2 == 0:
    print("I'm Sorry Hansoo")
else:
    answer = []
    candidates = sorted(counter.keys(), reverse=True)
    while candidates:
        candidate = candidates.pop()
        # 짝수 개면 절반 만큼 앞에 추가
        if counter[candidate] % 2 == 0:
            answer.append(candidate * (counter[candidate] // 2))
            del counter[candidate]
        # 홀수 개면 짝수만큼 추가하고 보류
        else:
            answer.append(candidate * (counter[candidate] // 2))
            counter[candidate] = 1
    part = ''.join(answer)
    if len(counter.keys()) == 1:
        print(part + list(counter.items())[0][0] + part[::-1])
    elif len(counter.keys()) > 1:
        print("I'm Sorry Hansoo")
    else:
        print(part + part[::-1])
