def solution(s):
    digits = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for d in digits:
        s = s.replace(d, str(digits.index(d)))

    return int(s)
