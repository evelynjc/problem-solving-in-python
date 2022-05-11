# 1641. Count Sorted Vowel Strings

https://leetcode.com/problems/count-sorted-vowel-strings/

```python
import math

class Solution:
    def countVowelStrings(self, n: int) -> int:
        r = n
        n = 4 + r
        return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))
```

- Combinations with repetitions
- Return nHr

count-sorted-vowel-strs
