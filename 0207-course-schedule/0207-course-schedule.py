from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {k: [] for k in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        traced = set()
        visited = set()

        def dfs(x):
            # 순환 구조이면 False
            if x in traced:
                return False
            # 이미 방문했던 노드라면 True
            if x in visited:
                return True
            # 순환 노드 추가
            traced.add(x)
            for pre in graph[x]:
                if not dfs(pre):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(x)
            # 탐색 종료 후 방문 노드 추가
            visited.add(x)
            return True

        for i in graph:
            if not dfs(i):
                return False

        return True
