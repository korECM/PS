class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        answers = []
        min_answer = sys.maxsize

        left, right = 0, 1
        check_map = Counter(s[0])
        target_map = Counter(t)
        while left < right:
            # 필요없는 문자 제거
            while left < len(s) and (check_map[s[left]] > target_map[s[left]] or right - left > min_answer):
                check_map[s[left]] -= 1
                left += 1

            if len(target_map - check_map) == 0:
                answers.append(s[left:right])
                min_answer = min(min_answer, right - left)

            # 문자열 추가
            if right < len(s):
                check_map[s[right]] += 1
                right += 1
            # 추가할 문자열이 없다면 왼쪽 증가
            elif left < len(s):
                check_map[s[left]] -= 1
                left += 1

        answers.sort(key=len)
        return answers[0] if answers else ""