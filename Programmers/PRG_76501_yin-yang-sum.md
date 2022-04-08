# 76501. 음양 더하기
https://programmers.co.kr/learn/courses/30/lessons/76501
```python
def solution(absolutes, signs):
    answer = list(map(lambda x, y: x * (-1) if y == 0 else x, absolutes, signs))
    return sum(answer)
```
- Used `map()` to get negative numbers.