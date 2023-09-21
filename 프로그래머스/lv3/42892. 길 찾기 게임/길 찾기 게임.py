import sys

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val, x, y, left=None, right=None):
        self.val = val
        self.x = x
        self.y = y
        self.left = left
        self.right = right

    def preorder(self, acc):
        acc.append(self.val)
        if self.left:
            self.left.preorder(acc)
        if self.right:
            self.right.preorder(acc)

    def postorder(self, acc):
        if self.left:
            self.left.postorder(acc)
        if self.right:
            self.right.postorder(acc)
        acc.append(self.val)


def sol(nodeinfo):
    if not nodeinfo:
        return None

    nodeinfo.sort(key=lambda x: x[2])

    root_info = nodeinfo.pop()
    
    root = Node(root_info[0], root_info[1], root_info[2])
    root.left = sol([(i, x, y) for i, x, y in nodeinfo if x < root.x])
    root.right = sol([(i, x, y) for i, x, y in nodeinfo if x > root.x])

    return root


def solution(nodeinfo):
    answer = [[], []]
    root = sol([(i + 1, a[0], a[1]) for i, a in enumerate(nodeinfo)])
    root.preorder(answer[0])
    root.postorder(answer[1])
    return answer
