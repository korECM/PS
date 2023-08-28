from sys import maxsize as ssm
from sys import stdin as ssi
from sys import stdout as sso

class IO:
    @staticmethod
    def input() -> str: return ssi.readline().rstrip()

    @staticmethod
    def num() -> int: return int(ssi.readline())

def is_group_word(s: str) -> bool:
    if len(s) == 1:
        return True
    char_set = set()
    for i in range(len(s)):
        c = s[i]
        if i == len(s) - 1:
            return c not in char_set or s[i] == s[i - 1]
        if c in char_set:
            if s[i] != s[i - 1]:
                return False
        else:
            char_set.add(c)


result = 0
for _ in range(IO.num()):
    s = IO.input()
    if is_group_word(s):
        result += 1
print(result)
