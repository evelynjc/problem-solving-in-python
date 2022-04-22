# 12982. 예산

https://programmers.co.kr/learn/courses/30/lessons/12982

```python
def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget - d[i] >= 0:
            answer += 1
        budget -= d[i]
    return answer
```

- Sort list in an ASC order so the condition `budget - d[i] >= 0` can be met as many times as possible
