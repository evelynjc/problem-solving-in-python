class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        acct_sum = [sum(act) for act in accounts]
        return max(acct_sum)
