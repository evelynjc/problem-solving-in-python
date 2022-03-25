# 5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return 1-letter or full-palindromic strings
        if len(s) == 1 or s == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            # check if the given string is palindromic and expand
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        result = ""
        # sliding window moving to the right
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result
```

**Success**\
Runtime: 250 ms, faster than 94.95% of Python3 online submissions for Longest Palindromic Substring.\
Memory Usage: 13.9 MB, less than 66.42% of Python3 online submissions for Longest Palindromic Substring.
