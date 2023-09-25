from collections import defaultdict, deque


def calc_diff(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
        if count > 1:
            return count
    return count

def solution(begin, target, words):
    data = defaultdict(list)
    for i in range(len(words) - 1):
        a = words[i]
        for j in range(i + 1, len(words)):
            b = words[j]
            if calc_diff(a,b) == 1:
                data[a].append(b)
                data[b].append(a)
    
    for i in range(len(words)):
        a = words[i]
        if calc_diff(a,begin) == 1:
            data[a].append(begin)
            data[begin].append(a)
    
    check_map = {begin: 0}
    queue = deque([(begin, 0)])
    while queue:
        word, count = queue.popleft()
        if word == target:
            return count
        for n in data[word]:
            if n not in check_map or check_map[n] > count + 1:
                check_map[n] = count + 1
                queue.append((n, count + 1))
    
    return 0