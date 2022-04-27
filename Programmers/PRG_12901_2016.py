def solution(a, b):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    day = sum(days_in_month[: a - 1]) + b
    return days_in_week[day % 7]
