def solution(places):
    answer = []
    m1a = [0, 0, 1, -1]
    m1b = [1, -1, 0, 0]
    m2a = [2, -2, 0, 0, 1, 1, -1, -1]
    m2b = [0, 0, 2, -2, -1, 1, -1, 1]

    for i in range(5):
        tmp = places[i]
        result = 1
        for j in range(5):
            for k in range(5):
                if(tmp[j][k] == "P"):
                    for a in range(4):
                        d1a = j + m1a[a]
                        d1b = k + m1b[a]
                        if(-1 < d1a < 5 and -1 < d1b < 5):
                            if(tmp[d1a][d1b] == "P"):
                                result = 0
                                break
                    for a in range(8):
                        d2a = j + m2a[a]
                        d2b = k + m2b[a]
                        if(-1 < d2a < 5 and -1 < d2b < 5):
                            if(tmp[d2a][d2b] == "P"):
                                if(abs(d2a - j) == 2):
                                    if(tmp[(d2a + j) // 2][d2b] == "O"):
                                        result = 0
                                        break
                                elif(abs(d2b - k) == 2):
                                    if(tmp[d2a][(d2b + k) // 2] == "O"):
                                        result = 0
                                        break
                                elif(tmp[d2a][k] == "O" or tmp[j][d2b] == "O"):
                                    result = 0
                                    break
                    if(result == 0):
                        break
                if(result == 0):
                        break
        answer.append(result)

    return answer
