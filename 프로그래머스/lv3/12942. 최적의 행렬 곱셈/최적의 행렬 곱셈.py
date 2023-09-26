import sys
sys.setrecursionlimit(10**6)

mem = {}

def sol(m, left, right):
    if right - left == 1:
        return 0, m[left][0], m[left][1]
    if right - left == 2:
        return m[left][0] * m[left][1] * m[left + 1][1],  m[left][0], m[left + 1][1]
    
    if (left ,right) not in mem:
        mem[(left, right)] = (sys.maxsize, 0,0)
    
        for i in range(left + 1, right):
            acc1, a, b = sol(m, left, i)
            acc2, c, d = sol(m, i, right)
            if mem[(left, right)][0] > acc1 + acc2 + a * b * d:
                mem[(left, right)] = (acc1 + acc2 + a * b * d, a, d)
    
    return mem[(left, right)]
        

def solution(m):
    return sol(m, 0, len(m))[0]