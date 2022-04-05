def solution(n):
    arr = ["4", "1", "2"]
    # base case
    if n < 4:
        return arr[n % 3]
    elif n % 3 == 0:
        return solution(n // 3 - 1) + arr[n % 3]
    else:
        return solution(n // 3) + arr[n % 3]
