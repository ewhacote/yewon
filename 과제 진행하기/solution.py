#문제 https://school.programmers.co.kr/learn/courses/30/lessons/176962

"""
스택을 활용한다
split(':'): 문자열을 특정 구분자를 기준으로 분리하는 메서드
map(int, ...): 주어진 iterable(여기서는 start.split(':')의 결과)의 모든 요소에 대해 지정된 함수(int())를 적용
"""

def solution(plans):
    plans.sort(key = lambda x: x[1]) #시작 시각에 따라 과제들을 정렬

    answer = [] # 결과 저장 리스트
    stack = []  # 현재 진행중인 과제(+멈춰둔 과제)를 저장할 스택

    for subject, start, time in plans:
        h, m = map(int, start.split(':'))
        start = 60*h+m  # 시작 시간을 분 단위로 변환
        time = int(time) # 과제 소요 시간을 정수로 변환
 
        if stack: #스택이 비어있지 않은 경우
            prev_subject, prev_start, prev_time = stack.pop()  # 이전에 진행 중이던 과제를 꺼냄 
            extra_time = start - prev_start # 새로운 과제 시작까지의 추가 시간 계산

            if extra_time < prev_time: # 추가 시간이 이전 과제의 남은 시간보다 적은 경우
                stack.append((prev_subject, prev_start, prev_time-extra_time)) # 남은 시간을 업데이트하여 스택에 다시 넣음
            else: # 추가 시간이 이전 과제의 남은 시간보다 크거나 같은 경우
                answer.append(prev_subject) # 이전 과제를 끝냄

                extra_time = extra_time - prev_time # 남은 추가 시간 업데이트

                while stack and extra_time : # 스택에 남은 과제가 있고, 남은 추가 시간이 있는 경우
                    prev_subject, prev_start, prev_time = stack.pop()

                    if extra_time < prev_time: # 남은 추가 시간이 현재 과제의 남은 시간보다 적은 경우
                        stack.append((prev_subject, prev_start, prev_time-extra_time))  # 남은 시간을 업데이트하여 스택에 다시 넣고 반복문 종료
                        break
                    else: # 남은 추가 시간이 현재 과제의 남은 시간보다 크거나 같은 경우
                        answer.append(prev_subject)  # 현재 과제를 끝냄
                        extra_time = extra_time - prev_time # 남은 추가 시간 업데이트

        stack.append((subject, start, time)) # 현재 과제를 스택에 넣음
 
    # 스택에 남은 과제들을 처리
    while stack:
        answer.append(stack.pop()[0])

    return answer