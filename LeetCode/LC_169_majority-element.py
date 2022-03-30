class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        # use a built-in function of Counter
        return Counter(nums).most_common(1)[0][0]
