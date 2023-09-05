from typing import List

def solution(n:int, arr1:List[int], arr2:List[int]):
    return [bin(a|b)[2:].rjust(n, "0").replace("1", "#").replace("0", " ") for a,b in zip(arr1, arr2)]