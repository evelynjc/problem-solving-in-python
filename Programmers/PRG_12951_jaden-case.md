# 12951. JadenCase 문자열 만들기

https://programmers.co.kr/learn/courses/30/lessons/12951

```python
def solution(s):
    # split words and put in a list
    s = s.split(" ")
    # turn the words into Jaden Case
    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return " ".join(s)
```
