# 92334. 신고 결과 받기

https://programmers.co.kr/learn/courses/30/lessons/92334

```python
def solution(id_list, report, k):
    d_report = {id: set() for id in id_list}
    reported, banned = [], []

    for r in report:
        r = r.split()
        d_report[r[0]].add(r[1])

    for v in d_report.values():
        reported.extend(v)
    banned = set(filter(lambda id: reported.count(id) >= k, id_list))

    return [len(banned & d_report[id]) for id in id_list]
```

- Data structures used: dictionary (hash) & set

### Steps:

1. Map the reporter user id and the reported user(s) in a `set` and put them into a `dict`\
   `(d_report = {id: {reported_user_1, reported_user_2}, ...})`
2. Merge `d_report.values()` to get all the users reported (duplicates allowed) and put them into `reported`
3. Count the number of reported times for each user and filter those are equal or bigger than `k`, put those into `banned`
4. For each id, count how many of the `banned` users they have reported by get the intersections of `banned` and `d_report[id]`
5. return the list of the result of Step 4
