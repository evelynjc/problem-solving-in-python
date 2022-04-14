# 451. Sort Characters By Frequency

https://leetcode.com/problems/sort-characters-by-frequency/

```python
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counted = dict(Counter(list(s)))

        answer = ""
        for k in sorted(counted.keys(), reverse=True, key=lambda x: counted[x]):
            answer += "".join(counted[k] * k)

        return answer
```

**Success**\
Runtime: 38 ms, faster than 95.07% of Python3 online submissions for Sort Characters By Frequency.\
Memory Usage: 16 MB, less than 33.57% of Python3 online submissions for Sort Characters By Frequency.
