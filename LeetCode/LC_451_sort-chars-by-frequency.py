from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counted = dict(Counter(list(s)))

        answer = ""
        for k in sorted(counted.keys(), reverse=True, key=lambda x: counted[x]):
            answer += "".join(counted[k] * k)

        return answer
