def solution(s):
    s_len = len(s)
    min_length = s_len
    for i in range(1, int(s_len / 2) + 1):
        result = ""
        temp = []
        start_position = 0
        while start_position < s_len:
            temp.append(s[start_position:start_position + i])
            start_position += i
        # print(temp)
        count = 1
        index = 0
        while index < len(temp):
            # print(f"index: {index}, count: {count}, result: {result}")
            if index == len(temp) - 1:
                if count > 1:
                    result += str(count)
                result += temp[index]
                break
            if temp[index] == temp[index + 1]:
                count += 1
            else:
                if count > 1:
                    result += str(count)
                result += temp[index]
                count = 1
            index += 1
        # print(result)
        min_length = min(min_length, len(result))
        # print(min_length)
    return min_length