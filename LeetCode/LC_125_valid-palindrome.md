# 125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = s.lower()

        # use regex to filter unused chars
        chars = re.findall(r'[a-z0-9]', s)

        # reverse char list
        return chars == chars[::-1]

        ## initial answer
        # chars_len = len(chars)
        # for i in range(chars_len // 2):
        #     if chars[i] != chars[chars_len-1-i]:
        #         return False
        # return True
```
**Success**\
Runtime: 40 ms, faster than  96.78%  of  Python3  online submissions for  Valid Palindrome.\
Memory Usage: 15.6 MB, less than  18.83%  of  Python3  online submissions for  Valid Palindrome.