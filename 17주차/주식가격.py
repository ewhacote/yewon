# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):

    times = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        for s,idx in stack:
            times[idx] += 1
        while stack and stack[-1][0] > prices[i]:
            stack.pop()
        stack.append((prices[i], i))

    return times
