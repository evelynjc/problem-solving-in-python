# 169 Majority Element

https://leetcode.com/problems/majority-element/

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        # use a built-in function of Counter
        return Counter(nums).most_common(1)[0][0]
```

**Success**\
Runtime: 186 ms, faster than 75.38% of Python3 online submissions for Majority Element.\
Memory Usage: 15.5 MB, less than 79.47% of Python3 online submissions for Majority Element.
