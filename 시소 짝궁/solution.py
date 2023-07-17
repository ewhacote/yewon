#문제 https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict


def solution(weights):
    answer = 0
    info = defaultdict(int)

    for w in weights:
        answer += info[w]
        answer += info[(w * 2) / 3] + info[(w * 3) / 2]
        answer += info[(w * 3) / 4] + info[(w * 4) / 3]
        answer += info[(w * 4) / 2] + info[(w * 2) / 4]
        info[w] += 1

    return answer