# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    stars = []
    
    # 교차점 찾기
    for i in range(len(line)):
        a,b,e = line[i]
        for j in range(i+1,len(line)):
            c,d,f = line[j]
            # 분모가 0인 경우
            if a*d - b*c == 0:
                continue
            # 분모가 0이 아닌 경우, 정수일 때만
            elif (b*f - e*d) / (a*d - b*c) == int((b*f - e*d) / (a*d - b*c)) and\
                (e*c - a*f) / (a*d - b*c) == int((e*c - a*f) / (a*d - b*c)):
                x = int((b*f - e*d) / (a*d - b*c))
                y = int((e*c - a*f) / (a*d - b*c))
                stars.append((x,y)) # 교점 리스트에 추가
    
    stars = list(set(stars)) # 중복 제거
    stars.sort(key=lambda x:(x[1],-x[0]),reverse=True) # x좌표 오름차순, y좌표 내림차순

    # x,y 최대,최소 구하기
    x_list = []
    y_list = []
    for i in stars:
        x_list.append(i[0])
        y_list.append(i[1])
    x_max = max(x_list) 
    x_min = min(x_list)
    y_max = max(y_list)
    y_min = min(y_list)

    # 좌표 초기화
    plaid = [['.' for _ in range(x_min,x_max+1)] for _ in range(y_min,y_max+1)]
    for i in stars:
        x = i[0] - x_min
        y = y_max - i[1] # x,y 좌표로 변경
        plaid[y][x] = '*' # y가 행, x가 열
    
    result = []
    for i in plaid: # 문자열로 합쳐서 결과 리스트에 추가
        result.append(''.join(i))
    return result
