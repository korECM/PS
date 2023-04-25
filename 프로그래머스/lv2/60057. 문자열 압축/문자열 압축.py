def solution(s):
    s_len = len(s)
    min_length = s_len
    for i in range(1, int(s_len / 2) + 1):
        result = ""
        chunks = chunk_str(s, i)
        count = 1
        for a, b in zip(chunks, chunks[1:] + [""]):
            if a == b:
                count += 1
            else:
                if count > 1:
                    result += str(count)
                result += a
                count = 1
        min_length = min(min_length, len(result))
    return min_length


def chunk_str(s, size):
    chunks = []
    start_position = 0
    while start_position < len(s):
        chunks.append(s[start_position:start_position + size])
        start_position += size
    return chunks