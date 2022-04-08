def solution(absolutes, signs):
    answer = list(map(lambda x, y: x * (-1) if y == 0 else x, absolutes, signs))
    return sum(answer)
