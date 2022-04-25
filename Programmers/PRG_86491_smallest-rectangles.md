# 86491. 최소직사각형

https://programmers.co.kr/learn/courses/30/lessons/86491

```python
def solution(sizes):
    answer = 0
    w, h = [], []
    for rect in sizes:
        rect.sort()
        w.append(rect[0])
        h.append(rect[1])
    return max(w)*max(h)
```
