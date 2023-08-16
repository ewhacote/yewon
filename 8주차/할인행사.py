"""
일정 금액 지불 10일 회원
매일 한가지 제품 할인 -> 하루에 하나씩
원하는 제품과 수량이 -> 10일 연속으로 일치할 경우

"""
def solution(want, number, discount):
    ans = 0
    wantList = dict()

    for i in range(len(want)):
        wantList[want[i]] = number[i]
    wantSet = set(wantList)

    for i in range(10):
        if discount[i] in wantList.keys():
            wantList[discount[i]] -= 1
            if wantList[discount[i]] == 0:
                wantSet.remove(discount[i])
    if len(wantSet) == 0:
        ans+=1        
    for j in range(10, len(discount)):

        if discount[j] in wantList.keys():
            wantList[discount[j]] -= 1
            if wantList[discount[j]] == 0:
                wantSet.remove(discount[j])


        if discount[j-10] in wantList.keys():
            wantList[discount[j-10]] += 1
            if wantList[discount[j-10]] == 1:
                wantSet.add(discount[j-10])

        if len(wantSet) == 0:
            ans+=1 

    return ans
