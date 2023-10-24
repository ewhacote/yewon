# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in citations:
        if i>answer:
            answer+=1
    return answer

