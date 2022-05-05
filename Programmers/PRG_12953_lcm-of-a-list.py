import math


def solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        while len(arr) > 2:
            a = arr.pop()
            b = arr.pop()
            arr.append(lcm(a, b))
        return lcm(arr[0], arr[1])


def lcm(a, b):
    return (a * b) // math.gcd(a, b)
