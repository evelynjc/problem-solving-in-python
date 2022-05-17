class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_bit = s.strip().split(" ")[-1]
        return len(last_bit)
