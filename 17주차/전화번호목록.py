# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    dic = {}
    for i in phone_book:
        dic[i] = 0
    #print(dic)
    for i in dic:
        for j in range(len(i)):
            if (i[:j] in dic):
                return False

    return True
