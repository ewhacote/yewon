# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/181188

"""
SOL1) s를 기준으로 정렬하여 해결
s를 기준으로 정렬 한 후, 윈도우를 이동해가면서 겹치는 부분이 없을 때마다 미사일을 발사한다
"""
def solution(targets):
    targets.sort(key=lambda x:x[0]) #행을 기준으로 리스트 정렬
    shoot = 0
    window = {'s':0, 'e':0} #윈도우 설정
    
    for target in targets:
        if window['e'] <= target[0]: #타겟 시작지점보다 윈도우 끝지점이 작을때 (겹치지 않을 때)
            shoot += 1 #미사일 발사
            window = {'s':target[0], 'e':target[1]}
        else:
            window = {'s': max(target[0], window['s']), 'e': min(target[1], window['e'])} 
    return shoot


"""
SOL2) e를 기준으로 정렬하여 해결
e를 기준으로 정렬 한 후, 마지막 미사일 발사한 지점을 기준으로 미사일을 발사한다.
"""
def solution2(targets):
    targets.sort(key=lambda x:x[1]) #열을 기준으로 리스트 정렬
    shoot = 0
    end=-1 #마지막 미사일 발사지점
    
    for target in targets:
        if end <= target[0]: #타겟 시작지점보다 마지막 미사일 발사지점이 작을때
            shoot += 1
            end=target[1]
    return shoot