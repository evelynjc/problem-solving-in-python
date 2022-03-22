# 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/submissions/
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}

        for word in strs:
            ordered_str = "".join(sorted(word))
            if ordered_str in str_dict.keys():
                str_dict[ordered_str].append(word)
            else:
                str_dict[ordered_str] = [word]

        anagrams = list(str_dict.values())
        return anagrams
```
**Success**\
Runtime: 117 ms, faster than 75.46% of Python3 online submissions for Group Anagrams.\
Memory Usage: 17.3 MB, less than 78.74% of Python3 online submissions for Group Anagrams.