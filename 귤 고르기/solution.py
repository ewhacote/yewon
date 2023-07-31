# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    answer = 0
    check = 0
    tangerine.sort()
    dup = {}
    for i in tangerine:
        if i in dup:
            dup[i] += 1
        else:
            dup[i] = 1

    arr = sorted(dup.items(), key=lambda x: x[1], reverse=True)
    if arr[0][1] >= k:
        return 1
    else:
        for i in arr:
            if check < k:
                check += i[1]
                answer += 1
            else:
                break
    return answer
