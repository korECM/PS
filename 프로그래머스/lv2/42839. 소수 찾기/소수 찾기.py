from itertools import permutations
from math import floor

def solution(numbers):
    answer = 0
    d = dict()
    
    for n in range(1, len(numbers) + 1):
        for k in permutations(numbers, n):
            if check(d, k):
                answer += 1
    
    return answer

def check(d, numbers):
    num = int("".join(numbers))
    if num in d: return False
    d[num] = 1
    return is_prime(num)


def is_prime(n):
    if n < 2: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    for i in range(3, floor(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True