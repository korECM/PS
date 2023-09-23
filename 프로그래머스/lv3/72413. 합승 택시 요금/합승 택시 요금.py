from collections import defaultdict
import sys

def solution(n, s, a, b, fares):
    graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
    for aa, bb, fare in fares:
        graph[aa][bb] = fare
        graph[bb][aa] = fare
    
    for k in range(1, n + 1):
        for aa in range(1, n + 1):
            for bb in range(1, n + 1):
                if aa == bb:
                    graph[aa][bb] = 0
                elif graph[aa][bb] > graph[aa][k] + graph[k][bb]:
                    graph[aa][bb] = graph[aa][k] + graph[k][bb]
                    
    answer = graph[s][a] + graph[s][b]
    for k in range(1, n + 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])
    
    return answer