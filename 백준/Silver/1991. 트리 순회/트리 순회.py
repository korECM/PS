import sys
from typing import Optional


def input() -> str:
    return sys.stdin.readline().rstrip()


def num_input() -> int:
    return int(input())


def nums_input():
    return map(int, input().split())

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


N = num_input()
tree = {}
for _ in range(N):
    a, b, c = input().split()
    b_node = TreeNode(b) if b != "." else None
    c_node = TreeNode(c) if c != "." else None
    a_node = tree[a] if a in tree else TreeNode(a)
    a_node.left = b_node
    a_node.right = c_node
    tree[a] = a_node
    tree[b] = b_node
    tree[c] = c_node

visited_preorder = []
visited_inorder = []
visited_postorder = []


def preorder(node: Optional[TreeNode]):
    if node:
        visited_preorder.append(node.val)
        preorder(node.left)
        preorder(node.right)


def inorder(node: Optional[TreeNode]):
    if node:
        inorder(node.left)
        visited_inorder.append(node.val)
        inorder(node.right)


def postorder(node: Optional[TreeNode]):
    if node:
        postorder(node.left)
        postorder(node.right)
        visited_postorder.append(node.val)


preorder(tree['A'])
print(''.join(visited_preorder))
inorder(tree['A'])
print(''.join(visited_inorder))
postorder(tree['A'])
print(''.join(visited_postorder))
