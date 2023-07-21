class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        str_set = set(s)
        for c in sorted(str_set):
            index = s.find(c)
            suffix = s[index:]
            if str_set == set(suffix):
                return c + self.removeDuplicateLetters(suffix.replace(c, ""))
