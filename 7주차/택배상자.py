# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    assist = []
    i = 1
    cnt = 0 
    while i != len(order)+1:
        assist.append(i)
        while assist and assist[-1] == order[cnt]:
            cnt += 1
            assist.pop()
            
        i += 1
    return cnt
