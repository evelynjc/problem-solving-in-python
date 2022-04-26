# 81301. 숫자 문자열과 영단어

https://programmers.co.kr/learn/courses/30/lessons/81301

```python
def solution(s):
    digits = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for d in digits:
        s = s.replace(d, str(digits.index(d)))

    return int(s)
```
