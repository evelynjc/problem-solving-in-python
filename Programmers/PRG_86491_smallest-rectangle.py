def solution(sizes):
    answer = 0
    w, h = [], []
    for rect in sizes:
        rect.sort()
        w.append(rect[0])
        h.append(rect[1])
    return max(w)*max(h)
