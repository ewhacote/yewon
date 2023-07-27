#문제 https://school.programmers.co.kr/learn/courses/30/lessons/142085

from heapq import heappush, heappop


def solution(n, k, enemy):
    hq = []
    for round, monster in enumerate(enemy):
        heappush(hq, monster)
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return round

    return len(enemy)
