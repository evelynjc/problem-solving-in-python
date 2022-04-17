# 42587. 프린터
https://programmers.co.kr/learn/courses/30/lessons/42587
```python
from collections import deque

def solution(priorities, location):
    ordered = []
    priorities = deque([(idx, val) for idx, val in enumerate(priorities)])

    while priorities:
        popped = priorities.popleft()
        # compare priorities' and popped's current values
        if list(filter(lambda x: x[1] > popped[1], priorities)):
            priorities.append(popped) # append to the last index
        else:
            ordered.append(popped) # printed

    return 1 + ordered.index(tuple(filter(lambda x: x[0] == location, ordered))[0])
```
- Used `list` & `deque` for queue/stack operations
- Used `filter()` to quickly get 