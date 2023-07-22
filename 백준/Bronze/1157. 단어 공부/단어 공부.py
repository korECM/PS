import sys
from collections import Counter


def input():
    return sys.stdin.readline().strip()


common = Counter(input().lower()).most_common(2)
if len(common) == 1:
    print(common[0][0].upper())
else:
    if common[0][1] == common[1][1]:
        print("?")
    else:
        print(common[0][0].upper())
