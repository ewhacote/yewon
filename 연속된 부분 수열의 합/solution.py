#문제 https://school.programmers.co.kr/learn/courses/30/lessons/178870

"""
비내림차순(오름차순) 정렬
[시작점, 끝점, 길이] -> 길이가 짧은 순으로 정렬 후 리턴
"""

def solution(sequence, k):
    n=len(sequence)
    
    sub_sum=0
    end=0
    
    answer = []
    for i in range(n):
        while sub_sum < k and end < n:
            sub_sum += sequence[end]
            end += 1
        if sub_sum==k:
            answer.append([i,end-1,end-1-i])
            
        sub_sum -= sequence[i]
    
    answer.sort(key=lambda x:x[2])
    return answer[0][:2]