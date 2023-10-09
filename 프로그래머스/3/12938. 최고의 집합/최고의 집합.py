from itertools import combinations_with_replacement

def get_mul(elements):
    acc = 1
    for e in elements:
        acc *= e
    return acc

def simple_solution(n, s):
    answer = -1
    comb = None
    
    for a in combinations_with_replacement(range(1, s + 1), n):
        if sum(a) == s:
            new_mul = get_mul(a)
            if answer < new_mul:
                answer = new_mul
                comb = a
            print(a)
    print(answer, comb)

def math_solution(n, s):
    answer = [s // n] * n
    
    for i in range(1, s % n + 1):
        answer[-i] += 1
    
    return answer

def solution(n, s):
    if n > s:
        return [-1]
    
#     for i in range(1, 10001):
#         for j in range(1, 100000001):
#             if simple_solution(i, j) != math_solution(i, j):
#                 print(i, j)
    
#     simple_solution(n, s)
    return math_solution(n, s)
    