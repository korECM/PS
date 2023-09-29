import sys
sys.setrecursionlimit(10**6)

mem = {}

def sol(n, money):
    if n > 0 and not money:
        return 0
    if n == 0:
        return 1
    
    if (n, len(money)) not in mem:
        if money[-1] > n:    
            mem[(n, len(money))] = sol(n, money[:-1])
        else:
            mem[(n, len(money))] = sol(n - money[-1], money) + sol(n, money[:-1])
    
    return mem[(n, len(money))]

def solution(n, money):
    return sol(n, sorted(money))
