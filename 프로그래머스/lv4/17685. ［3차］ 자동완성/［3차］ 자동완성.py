from collections import defaultdict

class TrieNode:
    word: bool
    clock: int
    
    def __init__(self):
        self.word = False
        self.clock = 0
        self.children = defaultdict(TrieNode)

class Trie:
    root: TrieNode
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        node = self.root
        for char in word:
            node.clock += 1
            node = node.children[char]
        node.word = True
        node.clock += 1
        
    def search(self, word: str):
        node = self.root
        count = 0
        for char in word:
            node = node.children[char]
            count += 1
            if node.clock == 1:
                return count
        return count
    
def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
        
    return sum([trie.search(word) for word in words])