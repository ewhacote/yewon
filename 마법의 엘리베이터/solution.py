#문제 https://school.programmers.co.kr/learn/courses/30/lessons/148653?language=python3

def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer
