from collections import deque


def solution(priorities, location):
    ordered = []
    priorities = deque([(idx, val) for idx, val in enumerate(priorities)])

    while priorities:
        popped = priorities.popleft()
        if list(filter(lambda x: x[1] > popped[1], priorities)):
            priorities.append(popped)
        else:
            ordered.append(popped)

    return 1 + ordered.index(tuple(filter(lambda x: x[0] == location, ordered))[0])
