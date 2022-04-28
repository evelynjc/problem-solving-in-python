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
