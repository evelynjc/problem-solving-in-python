# 12953. N개의 최소공배수

https://programmers.co.kr/learn/courses/30/lessons/12953

```python
import math

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        while len(arr) > 2:
            a = arr.pop()
            b = arr.pop()
            arr.append(lcm(a, b))
        return lcm(arr[0], arr[1])

def lcm(a, b):
    return (a * b) // math.gcd(a, b)
```
- Pair 2 elements in `arr` and replace them with their **LCM** until `arr` has only 2 elements.
- Return the **LCM** of shortened `arr`.