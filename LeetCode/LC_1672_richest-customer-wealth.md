# 1672. Richest Customer Wealth

https://leetcode.com/problems/richest-customer-wealth/

```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        acct_sum = [sum(act) for act in accounts]
        return max(acct_sum)
```

**Success**\
Runtime: 52 ms, faster than 95.55% of Python3 online submissions for Richest Customer Wealth.\
Memory Usage: 14 MB, less than 35.14% of Python3 online submissions for Richest Customer Wealth.
