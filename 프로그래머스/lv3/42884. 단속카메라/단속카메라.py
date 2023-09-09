def solution(routes):
    routes.sort()
    
    temp = [routes.pop()]
    while routes:
        # left 같거나 작거나
        # right 같거나 작거나
        if routes[-1][1] < temp[-1][0]:
            temp.append(routes.pop())
        else:
            left = max(routes[-1][0], temp[-1][0])
            right = min(routes[-1][1], temp[-1][1])
            temp[-1] = [left, right]
            routes.pop()
    return len(temp)