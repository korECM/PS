import heapq

add, del_max, del_min = "add", "del_max", "del_min"

def parse(op_str):
    ops = op_str.split(" ")
    num = int(ops[1])
    if ops[0] == "I":
        return add, num
    else:
        if num == 1:
            return del_max, 0
        return del_min, 0

class DoublePQ:
    def __init__(self):
        self.index = 0
        self.processed_set = set()
        self.max_queue = []
        self.min_queue = []
        
    def add(self, num):
        heapq.heappush(self.max_queue, (-num, self.index))
        heapq.heappush(self.min_queue, (num, self.index))
        self.index += 1
        
    def del_min(self):
        if self.min_queue:
            _, index = heapq.heappop(self.min_queue)
            self.processed_set.add(index)
        self.clean()
                
    def del_max(self):
        if self.max_queue:
            _, index = heapq.heappop(self.max_queue)
            self.processed_set.add(index)
        self.clean()
    
    def clean(self):
        while self.max_queue and self.max_queue[0][1] in self.processed_set:
            heapq.heappop(self.max_queue)
        while self.min_queue and self.min_queue[0][1] in self.processed_set:
            heapq.heappop(self.min_queue)
    
    def get_min_max(self):
        answer = []
        self.clean()
        if not self.max_queue:
            return [0, 0]
        return [-self.max_queue[0][0], self.min_queue[0][0]]

def solution(operations):
    queue = DoublePQ()
    
    for op in operations:
        action, num = parse(op)
        if action == add:
            queue.add(num)
        elif action == del_min:
            queue.del_min()
        else:
            queue.del_max()
    
    return queue.get_min_max()