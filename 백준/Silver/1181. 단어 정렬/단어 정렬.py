import sys


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


n = num_input()
words = []
dict = {}
for _ in range(n):
    word = input()
    if word not in dict:
        words.append(word)
        dict[word] = 1
words.sort(key=lambda w: (len(w), w))
for word in words:
    print(word)
