# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque


def solution(people, limit):
    answer = 0
    dq = deque()

    # 오름차순으로 정렬
    arr=sorted(people)

    for i in range(0, len(arr)):
        dq.append(arr[i])


    front = 0

    while(len(dq) > 1):
        if(dq[front] + dq[-1] > limit):
            answer += 1
            dq.pop()

        else:
            dq.pop()
            dq.popleft()
            answer+=1

    if(len(dq) == 1):       
        dq.popleft()
        answer+=1


    return answer
