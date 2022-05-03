# 77484. 로또의 최고 순위와 최저 순위
https://programmers.co.kr/learn/courses/30/lessons/77484
```python
def solution(lottos, win_nums):
    ranks = [6, 6, 5, 4, 3, 2, 1]
    matches = set(lottos) & set(win_nums)
    print(matches, len(matches))
    highest = ranks[len(matches) + lottos.count(0)]
    lowest = ranks[len(matches)]
    return [highest, lowest]
```