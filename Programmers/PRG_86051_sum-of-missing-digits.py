def solution(numbers):
    nine_to_zero = [digit for digit in range(0, 10)]
    numbers = list(filter(lambda x: x not in numbers, nine_to_zero))

    return sum(numbers)
