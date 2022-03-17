import re

s = s.lower()

# use regex to filter unused chars
chars = re.findall(r'[a-z0-9]', s)

return chars == chars[::-1]

## initial answer
# chars_len = len(chars)
# for i in range(chars_len // 2):
#     if chars[i] != chars[chars_len-1-i]:
#         return False
# return True
