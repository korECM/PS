sheep, wolf = 0, 1

class Node:
    
    def __init__(self, num, kind, parent = None, left = None, right = None):
        self.num = num
        self.kind = kind
        self.left = left
        self.right = right
        self.parent = parent
    
    def add_child(self, child):
        if self.left is None:
            self.left = child
        else:
            self.right = child
    
    def get_children(self):
        return [c for c in [self.left, self.right] if c is not None]
    
    def set_parent(self, parent):
        self.parent = parent
    
    def is_sheep(self):
        return self.kind == sheep

def find(nodes, sheep_count, wolf_count, target):
    # 먼저 남은 양부터 다 방문
    while True:
        flag = True
        for t in target[:]:
            if t.is_sheep():
                flag = False
                target.remove(t)
                sheep_count += 1
                target.extend(t.get_children())
        if flag:
            break
    # print(sheep_count, [a.num for a in target])
    result = sheep_count
    for i in range(len(target)):
        if sheep_count > wolf_count + 1:
            # print(f'go {target[i].num}')
            result = max(result, find(nodes, sheep_count,wolf_count + 1, target[:i] + target[i+1:] + target[i].get_children()))
            # print(f'backtrack {target[i].num}')
    
    return result
    
        
def solution(info, edges):
    nodes = [Node(i, kind) for i, kind in enumerate(info)]
    for p, c in edges:
        nodes[p].add_child(nodes[c])
        nodes[c].set_parent(nodes[p])
    return find(nodes, 0, 0, [nodes[0]])