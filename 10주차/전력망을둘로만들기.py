# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    answer = -1
    saveWires = wires.copy()
    countList = []
    count = 0

    for comb in wires.copy():
        saveWires.remove(comb)
        setl = set([comb[0]])
        previous = set()
        while (setl != previous) :
            previous = setl.copy()
            for wire in saveWires.copy():
                if (setl & set(wire)):
                    setl = setl | set(wire)
        countList.append(abs((n - 2*len(setl))))
        count = 0
        saveWires = wires.copy()

    answer = min(countList)
    return answer
