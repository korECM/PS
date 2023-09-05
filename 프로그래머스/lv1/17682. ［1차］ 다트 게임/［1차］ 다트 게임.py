def get_score(s: str):
    if s[0] == "1" and s[1] == "0":
        return s[2:], 10
    return s[1:], int(s[0])

def get_area(s: str):
    if s[0] == "S":
        return s[1:], 1
    if s[0] == "D":
        return s[1:], 2
    if s[0] == "T":
        return s[1:], 3
    

def get_option(s: str):
    if s and s[0] in "*#":
        return s[1:], s[0]
    return s, "N"

def solution(dartResult: str):
    answer = 0
    prev_score = 0
    for i in range(3):
        dartResult, score = get_score(dartResult)
        dartResult, area = get_area(dartResult)
        dartResult, option = get_option(dartResult)
        
        cur_score = score
        cur_score **= area
        
        if option == "*":
            prev_score *= 2
            cur_score *= 2
        elif option == "#":
            cur_score *= -1
        
        answer += prev_score
        prev_score = cur_score
    return answer + prev_score