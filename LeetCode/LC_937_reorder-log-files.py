class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        import re

        letters, digits = [], []

        for log in logs:
            if re.match(r'(\w+\s)([a-z]+\s*)+', log):
                letters.append(log)
            else:
                digits.append(log)

        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits