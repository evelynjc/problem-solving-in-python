# 937. Reorder Data in Log Files
https://leetcode.com/problems/reorder-data-in-log-files/
```python
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
```
**Success**\
Runtime: 79 ms, faster than 7.33% of Python3 online submissions for Reorder Data in Log Files.\
Memory Usage: 14 MB, less than 82.53% of Python3 online submissions for Reorder Data in Log Files.