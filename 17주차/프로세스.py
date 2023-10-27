# 문제https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque, Counter

def solution(priorities, location):
    counter = Counter(priorities)
    rank = sorted(counter.keys(), key=lambda x: x)
    length = len(priorities)

    q = deque()
    for i in range(length):
        q.append((i, priorities[i]))

    cnt = 1
    while q:
        # First cmd
        idx, prior = q.popleft()

        # Second cmd
        if prior < rank[-1]:
            q.append((idx, prior))
            continue

        # Exit condition
        if idx == location:
            return cnt

        # Third cmd
        counter[prior] -= 1
        cnt += 1

        if counter[prior] == 0:
            del counter[prior]
            rank.pop()
