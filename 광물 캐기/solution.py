# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/172927

'''
아이디어
알고리즘 (정렬, 그리디)

일단 가지고 있는 곡갱이를 사용하여 모든 광물을 캘 수 있는지 체크한다
1) 모두 캘 수 없는 경우 : minerals를 캘 수 있는 만큼의 자원까지만 자름. ex) minerals[:5 * sum(picks)]
2) 모두 캘 수 있는 경우 : minerals를 그대로 들고 갑니다.

자원을 5개 단위로 나누어 그 묶음을 다이아 곡갱이로 캘 때, 철 곡갱이로 캘 때, 돌 곡갱이로 캘 때 피로도를 계산하여 리스트로 따로 저장한다. 
[다이아 곡갱이로 5개를 다 캘 때 피로도, 철 곡갱이로 다 캘 때 피로도, 돌 곡갱이로 다 캘 때 피로도]를 저는 info라는 리스트에 저장
이 것을 minerals의 끝까지 돌려줍니다. -> 첫 번째 예시의 경우 info = [[5, 17, 85], [3, 7, 31]] 이런 식으로 넣어집니다.

리스트 안의 값을 보았을 때 돌 곡갱이로 캘 때 피로도가 제일 큰 값인 경우 -> 다이아 곡갱이로 캐는 게 효율이 좋습니다.
위의 예시로 보면 info에 첫 번째 묶음은 [5,17,85]이고 두 번째 묶음은 [3,7,31]인데 첫 번째 묶음의 경우 돌 곡갱이로 캐는 경우 피로도가 85이므로 가지고 있는 가장 좋은 곡갱이로 캐는 게 효율이 좋습니다.
이를 한번의 알 기 위해 info 리스트를 돌 곡갱이 피로도, 철 곡갱이 피로도, 다이아 곡갱이 피로도 순으로 info를 정렬을 해줍니다.

정렬된 info 리스트를 뒤에서부터 pop 해오면서 가지고 있는 가장 좋은 곡갱이들부터 차례로 사용하면서 피로도를 계산해줍니다.
'''

from collections import deque
def solution(picks, minerals):

    answer = 0
    tiredList = [[1,1,1],[5,1,1],[25,5,1]]
    connectionDict = {
        "diamond":0,
        "iron" : 1,
        "stone" : 2
    }
    info = []
    minerals = minerals[:5 * sum(picks)]
    q = deque(minerals)
    while q:
        howManyDig = 0
        usedDia, usedIron, usedStone = 0,0,0
        while howManyDig < 5:
            howManyDig += 1
            mineral = q.popleft()
            usedDia += tiredList[0][connectionDict[mineral]]
            usedIron += tiredList[1][connectionDict[mineral]]
            usedStone += tiredList[2][connectionDict[mineral]]
            if not q:
                break
        info.append([usedDia,usedIron,usedStone])
    info.sort(key = lambda x : [x[2],x[1],x[0]])

    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer += info.pop()[idx]
            else:
                return answer

    return answer



# deque 사용 안할 경우
def solution(picks, minerals):
    tired=[[1,1,1],[5,1,1],[25,5,1]]
    conn={"diamond":0, "iron":1, "stone":2}
    
    minerals=minerals[: 5*sum(picks)]
    answer = 0
    info=[]

    while minerals:
        count=0
        d_used, i_used, s_used=0,0,0
        while count <5:
            count+=1
            mineral=minerals.pop(0)
            d_used+=tired[0][conn[mineral]]
            i_used+=tired[1][conn[mineral]]
            s_used+=tired[2][conn[mineral]]
            if not minerals:
                break
        info.append([d_used,i_used,s_used])
    info.sort(key=lambda x:[x[2],x[1],x[0]])
    
    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer+=info.pop()[idx]
            else:
                return answer
    return answer
