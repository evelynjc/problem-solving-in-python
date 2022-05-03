def solution(lottos, win_nums):
    ranks = [6, 6, 5, 4, 3, 2, 1]
    matches = set(lottos) & set(win_nums)
    print(matches, len(matches))
    highest = ranks[len(matches) + lottos.count(0)]
    lowest = ranks[len(matches)]
    return [highest, lowest]
