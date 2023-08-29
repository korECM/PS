from collections import deque
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = [None for _ in range(len(people))]
        people.sort(key=lambda x: (x[0], x[1]), reverse=True)
        while people:
            target = deque([people.pop()])
            while people and target[0][0] == people[-1][0]:
                target.append(people.pop())
            index, count = 0, 0
            while target and index < len(answer):
                if count == target[0][1] and answer[index] is None:
                    answer[index] = target.popleft()
                    count += 1
                elif answer[index] is None:
                    count += 1
                index += 1
        return answer
