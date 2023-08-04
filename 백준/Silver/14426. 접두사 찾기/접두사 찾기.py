import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def num_input():
    return int(input())


def nums_input():
    return map(int, input().split())


class TrieNode:
    word: bool
    children: dict[str, object]

    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)


class Trie:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()

n, m = nums_input()
for i in range(n):
    trie.insert(input())
count = 0
for i in range(m):
    count += 1 if trie.startsWith(input()) else 0
print(count)
