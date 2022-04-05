# 12947. 하샤드 수

https://programmers.co.kr/learn/courses/30/lessons/12947

```python
def solution(x):
    digit_sum = 0

    for elem in list(str(x)):
        digit_sum += int(elem)

    return x % digit_sum == 0
```

1. Split the given number `x` into individual digits.
2. `digit_sum` holds the sum of the digits.
3. Return `True` when `x` is divisible by `digit_sum`, and `False` otherwise.
