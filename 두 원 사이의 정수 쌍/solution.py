#문제 https://school.programmers.co.kr/learn/courses/30/lessons/181187

"""
1사분면의 정수 쌍 개수를 구한 뒤 4를 곱한다 (이 때 겹치는 점이 없도록 해야 함)
1부터 r2까지 각 x값마다 y정수 범위를 구한다
"""

from math import floor,ceil,sqrt
def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        max_y=floor(sqrt(r2**2-x**2))
        if x>r1: #sqrt함수에 음수가 들어가면 에러 발생
            min_y=0
        else:
            min_y=ceil(sqrt(r1**2-x**2))
        answer+=max_y-min_y+1
    return answer*4