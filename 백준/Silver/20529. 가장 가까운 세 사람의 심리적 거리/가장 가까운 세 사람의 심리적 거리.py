import sys
from collections import defaultdict, Counter
from itertools import combinations, combinations_with_replacement
from typing import TypeVar


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

dist_map = defaultdict(dict)
dist_map2 = defaultdict(dict)

for a, b in combinations_with_replacement(mbti_types, 2):
    dist = len(set(a) - set(b))
    dist_map[a][b] = dist
    dist_map[b][a] = dist
    if dist not in dist_map2[a]:
        dist_map2[a][dist] = set()
    dist_map2[a][dist].add(b)
    if dist not in dist_map2[b]:
        dist_map2[b][dist] = set()
    dist_map2[b][dist].add(a)


def solve(n: int, mbti_list: list[str]):
    # 같은 MBTI 3개 있는 경우
    if n >= 16 * 3:
        return 0

    answer = sys.maxsize
    counter = Counter(mbti_list)
    most_common_list = counter.most_common()
    if most_common_list[0][1] >= 3:
        return 0
    for mbti, count in most_common_list:
        # 2개 중복 있는 경우
        if count == 2:
            # 거리 1~4
            for i in range(1, 5):
                for target in dist_map2[mbti][i]:
                    if target in counter:
                        answer = min(answer, i * 2)
        else:
            break
    # mbti 중복 없음
    # n 최대 16
    for a, b, c in combinations(counter.keys(), 3):
        answer = min(answer, dist_map[a][b] + dist_map[a][c] + dist_map[b][c])
    return answer


for _ in range(num_input()):
    n = num_input()
    mbti = input().split()
    print(solve(n, mbti))
