# 58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/submissions/
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_bit = s.strip().split(" ")[-1]
        return len(last_bit)
```
**Success**\
Runtime: 41 ms, faster than 51.35% of Python3 online submissions for Length of Last Word.\
Memory Usage: 14.1 MB, less than 5.60% of Python3 online submissions for Length of Last Word.