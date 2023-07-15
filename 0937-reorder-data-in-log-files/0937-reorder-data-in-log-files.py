class Solution:
    def reorderLogFiles(self, logs):
        digits = []
        letters = []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda str: (str.split()[1:], str.split()[0]))
        return letters + digits

