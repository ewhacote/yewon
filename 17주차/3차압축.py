# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):    
    dict = {}

    for num in range(0, 26):
        alpha = chr(num + 65)
        dict[alpha] = num + 1

    # A ~ Z 사전을 만들어준다.


    answer = [0]
    value = 26
    base = ""

    for i in range(len(msg)):
        base += msg[i]
        if not base in dict:
            value += 1
            dict[base] = value

            base = msg[i]
            answer.append(dict[base])
            # 사전에 없다면 사전에 추가하고, base를 msg[i]로 변경한다.
        else:
            answer[-1] = dict[base]
            # base가 사전에 있다면 answer에 마지막으로 추가한 숫자를 변경해준다.


    return answer
