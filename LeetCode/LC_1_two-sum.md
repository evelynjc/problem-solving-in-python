# 1. Two Sum

https://leetcode.com/problems/two-sum/

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i, num in enumerate(nums):
            if target - num in mapped:
                return [mapped[target - num], i]
            mapped[num] = i
```

**Success**\
Runtime: 141 ms, faster than 38.95% of Python3 online submissions for Two Sum.\
Memory Usage: 15.1 MB, less than 63.62% of Python3 online submissions for Two Sum.
