# 86051. 없는 숫자 더하기

https://programmers.co.kr/learn/courses/30/lessons/86051

```python
def solution(numbers):
    nine_to_zero = [digit for digit in range(0, 10)]
    numbers = list(filter(lambda x: x not in numbers, nine_to_zero))

    return sum(numbers)
```
1. Create a list containing all digits.
2. Use `filter()` to find missing digits and get the sum.