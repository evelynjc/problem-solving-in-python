# 42. Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        blocks, units = sum(height), 0
        r_height = height[::-1]

        # calculate at each height
        for h in range(1, max(height) + 1):
            # get the first index of a value >= h
            start = height.index(next(elem for elem in height if elem >= h))
            # get the last index of a value >= h
            end = (
                len(height)
                - 1
                - r_height.index(next(elem for elem in r_height if elem >= h))
            )
            units += end - start + 1

        return units - blocks
```

**Success**\
Runtime: 9557 ms, faster than 5.03% of Python3 online submissions for Trapping Rain Water.\
Memory Usage: 15.6 MB, less than 90.30% of Python3 online submissions for Trapping Rain Water.
