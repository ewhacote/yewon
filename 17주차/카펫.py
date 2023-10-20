# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # 총 블록 수
    allBlock = brown + yellow

    # 초기 가로, 세로 길이
    width = 3
    height = 1

    while True:
        # 총 블록수 / 가로길이 --> 몫, 나머지
        height = allBlock // width
        remainder = allBlock % width

        # 나머지 0이고 가로 길이 >= 세로 길이 이고
        # 중앙 블록 (가로 -2 * 세로 - 2) == 노랑 블록 수 이면 해당 가로,세로 길이 값 리턴
        if remainder == 0 and width >= height and yellow == (width-2) * (height-2):
            return [width, height]

        # 그게 아니면 가로 길이 +1
        width += 1
