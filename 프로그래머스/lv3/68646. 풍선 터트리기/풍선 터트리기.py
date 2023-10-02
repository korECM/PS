left_min = {}
right_min = {}

def solution(elements):
    if len(elements) <= 2:
        return len(elements)
    
    answer = len(elements)
    
    cur = 1000000001
    for i in range(len(elements)):
        cur = min(cur, elements[i])
        left_min[i] = cur
    
    cur = 1000000001
    for i in range(len(elements) - 1, -1, -1):
        cur = min(cur, elements[i])
        right_min[i] = cur
    
    # 처음, 마지막 제외
    for i in range(1, len(elements) - 1):
        # i번째 원소 확인
        left_part = left_min[i]
        right_part = right_min[i + 1]
        if left_part < elements[i] and right_part < elements[i]:
            answer -= 1
    
    return answer