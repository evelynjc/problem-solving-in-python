# 62048. 멀쩡한 사각형

https://programmers.co.kr/learn/courses/30/lessons/62048

```python
import math
def solution(w,h):
    gcd_wh = math.gcd(w, h)
    affected_cnt = gcd_wh * ((w + h) / gcd_wh - 1)
    return (w * h) - affected_cnt
```

- Get GCD of w, h
- Get the number of affected cells for the rectangle w/GCD \* h/GCD
- Number of affected cells = (w + h - 1) \* GCD
