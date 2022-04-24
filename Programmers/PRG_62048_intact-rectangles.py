import math
def solution(w,h):
    gcd_wh = math.gcd(w, h)
    affected_cnt = gcd_wh * ((w + h) / gcd_wh - 1)
    return (w * h) - affected_cnt
