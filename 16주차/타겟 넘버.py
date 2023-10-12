# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):

    def calc(idx, sum):
        nonlocal answer

        if idx == len(numbers):
            if sum == target:
                answer += 1
            return

        calc(idx+1, sum + numbers[idx])
        calc(idx+1, sum - numbers[idx])

    answer = 0
    calc(0, 0)

    return answer
