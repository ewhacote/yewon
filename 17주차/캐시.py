#문제 https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque


def solution(cacheSize, cities):
    dq = deque(maxlen=cacheSize)
    run_time = 0
    for city in cities:
        city = city.lower()
        if city not in dq: # cache miss
            dq.append(city)
            run_time += 5
        else: # cache hit
            dq.remove(city)
            dq.append(city)
            run_time += 1

    return run_time
