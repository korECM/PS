N = int(input())
index = 0
answer = 0
while N:
    if N % 2 == 1:
        answer += 3 ** index
    index += 1
    N //= 2
print(answer)
