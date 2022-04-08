import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)

    mixes, max_iter = 0, len(scoville) - 1
    while scoville[0] < K and mixes < max_iter:
        popped_first = hq.heappop(scoville)
        popped_second = hq.heappop(scoville)
        hq.heappush(scoville, popped_first + (2 * popped_second))
        mixes += 1

    if scoville[0] >= K:
        return mixes
    else:
        return -1
