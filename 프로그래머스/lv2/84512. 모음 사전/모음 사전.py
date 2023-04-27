import sys

sys.setrecursionlimit(10000)

next_word = {
    "A": "E",
    "E": "I",
    "I": "O",
    "O": "U",
    "U": None
}


def solution(word):
    return s("A", word, 1)


def s(word, target, count):
    if word == target:
        return count
    if len(word) < 5:
        return s(word + "A", target, count + 1)
    else:
        while True:
            next_word_target = next_word[word[-1]]
            if next_word_target is not None:
                break
            word = word[:-1]
        return s(word[:-1] + next_word_target, target, count + 1)
