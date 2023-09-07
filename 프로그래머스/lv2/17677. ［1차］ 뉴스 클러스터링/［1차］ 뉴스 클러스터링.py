from collections import defaultdict

def calc(a_d, b_d):
    if not a_d and not b_d:
        return 1
    intersect_ab = {}
    union_ab = {}
    for a in a_d:
        if a in b_d:
            intersect_ab[a] = min(a_d[a], b_d[a])
            union_ab[a] = max(a_d[a], b_d[a])
        else:
            union_ab[a] = a_d[a]
    for b in b_d:
        if b not in a_d:
            union_ab[b] = b_d[b]
    return sum(intersect_ab.values()) / sum(union_ab.values())

def get_set(raw_str):
    a = defaultdict(int)
    for i in range(len(raw_str) - 1):
        s = raw_str[i:i+2]
        if s[0].isalpha() and s[1].isalpha():
            a[s.lower()] += 1
    return a

def solution(str1, str2):
    answer = 0
    return int(calc(get_set(str1), get_set(str2)) * 65536)