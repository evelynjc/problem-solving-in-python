# 136. Single Number

https://leetcode.com/problems/single-number/

```python
# one liner using dictionary comprehension
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return {v: k for k, v in dict(Counter(nums)).items()}[1]
```

**Success**\
Runtime: 136 ms, faster than 90.80% of Python3 online submissions for Single Number.\
Memory Usage: 16.5 MB, less than 94.04% of Python3 online submissions for Single Number.
