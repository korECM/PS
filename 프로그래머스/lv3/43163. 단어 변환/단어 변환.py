from collections import defaultdict, deque
from itertools import combinations


def calc_diff(a, b):
    count = 0
    for w1, w2 in zip(a, b):
        if w1 != w2:
            count += 1
        if count > 1:
            return count
    return count


def solution(begin, target, words):
    word_connection = defaultdict(list)
    for a, b in combinations(words + [begin], 2):
        if calc_diff(a, b) == 1:
            word_connection[a].append(b)
            word_connection[b].append(a)

    dp_map = {begin: 0}
    queue = deque([(begin, 0)])
    while queue:
        word, count = queue.popleft()
        if word == target:
            return count

        new_count = count + 1
        for next in word_connection[word]:
            if next not in dp_map or dp_map[next] > new_count:
                dp_map[next] = new_count
                queue.append((next, new_count))

    return 0
