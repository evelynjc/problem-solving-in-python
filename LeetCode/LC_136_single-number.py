# one liner using dictionary comprehension
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return {v: k for k, v in dict(Counter(nums)).items()}[1]
