class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = []
        for i in s:
            if i.isalnum():
                ch.append(i.lower())
        s = "".join(ch)
        return s == "".join(reversed(s))