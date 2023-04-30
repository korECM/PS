def solution(brown, yellow):
    answer = []
    
    for h in range(3, 5000//2):
        for w in range(h, 5000 // 2):
            if 2 * (w + h) - 4 != brown:
                continue
            if (w - 2) * (h - 2) == yellow:
                return [w, h]