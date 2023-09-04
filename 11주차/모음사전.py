def solution(word):
    answer = 0
    plist = ['A','E','I','O','U']
    vnum = len(plist)
    mlist = [vnum**x for x in range(0,vnum)]
    slist = [sum(mlist[:x]) for x in range(1,vnum+1)]
    skey = len(slist) - 1
    xsum = 0
    for x in word:
        xsum += plist.index(x)*slist[skey] + 1
        skey -= 1
    answer = xsum
    return answer
