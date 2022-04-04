def solution(x):
    digit_sum = 0
    
    for elem in list(str(x)):
        digit_sum += int(elem)
    
    return x % digit_sum == 0
