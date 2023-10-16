# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    # answer 리스트 및 nameMap 딕셔너리 선언
    answer = []
    nameMap = dict()
 
    # nameMap에 key값은 id, Value는 nickName
    # nickName 값은 가장 마지막으로 수정한 값을 저장
    for s in record:
        L = s.split()
 
        if L[0] == "Leave":
            continue
 
        nameMap[L[1]] = L[2]
 
    # 다시 한번 record 배열만큼 반복문 돌면서
    # Enter, Leave에 한해서 nameMap에 저장된 닉네임으로
    # answer 배열에 추가한다.
    for s in record:
        L = s.split()     
 
        if L[0] == "Enter":
            answer.append(nameMap[L[1]] + "님이 들어왔습니다.")
 
        elif L[0] == "Leave":
            answer.append(nameMap[L[1]] + "님이 나갔습니다.")
 
    return answer
