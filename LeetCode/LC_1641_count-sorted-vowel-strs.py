import math


class Solution:
    def countVowelStrings(self, n: int) -> int:
        r = n
        n = 4 + r
        return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))
