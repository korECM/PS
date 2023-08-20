a, b, c = map(int, input().split())
result = 1
while b:
    b, one = divmod(b, 2)
    if one:
        result = (result * a) % c
    a = (a * a) % c
print(result)
