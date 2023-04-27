def solution(s):
    answer = [0, 0]
    while s != "1":
        one_count = 0
        for l in s:
            if l == "1":
                one_count += 1
        answer[1] += len(s) - one_count
        s = radix_change(one_count, 2)
        answer[0] += 1
    
    return answer

def radix_change(num, radix):
    if num == 0: return '0'
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return "".join(reversed(nums))