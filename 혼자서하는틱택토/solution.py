#문제 https://school.programmers.co.kr/learn/courses/30/lessons/160585

from collections import defaultdict


def solution(board):
    counts = defaultdict(int)

    for r in range(len(board)):
        for c in range(len(board[0])):
            grid = board[r][c]
            counts[grid] += 1

    if counts["O"] == 0 and counts["X"] == 0:
        return 1

    if not (counts["O"] == counts["X"] or counts["O"] == counts["X"] + 1):
        return 0

    first_is_winner = second_is_winner = False

    for row in board:
        if all(grid == "O" for grid in row):
            first_is_winner = True
        if all(grid == "X" for grid in row):
            second_is_winner = True

    for col in zip(*board):
        if all(grid == "O" for grid in col):
            first_is_winner = True
        if all(grid == "X" for grid in col):
            second_is_winner = True

    diagonal = [board[r][c] for r in range(len(board)) for c in range(len(board[0])) if r == c]
    if all(grid == "O" for grid in diagonal):
        first_is_winner = True
    if all(grid == "X" for grid in diagonal):
        second_is_winner = True

    rev_diagonal = [board[r][c] for r in range(len(board)) for c in range(len(board[0])) if r + c + 1 == len(board)]
    if all(grid == "O" for grid in rev_diagonal):
        first_is_winner = True
    if all(grid == "X" for grid in rev_diagonal):
        second_is_winner = True

    if first_is_winner and second_is_winner:
        return 0
    else:
        if first_is_winner and not second_is_winner and counts["O"] == counts["X"]:
            return 0
        elif not first_is_winner and second_is_winner and counts["O"] == counts["X"] + 1:
            return 0

    return 1


# 추가 풀이

"""
틱택토가 맞는 규칙
1. O가 선공이기 때문에 X와 개수가 같거나 O가 1개 더 많아야 함.
2. O와 X가 둘다 3개가 연속으로 있을 수 없다.
3. O가 이겼다면 O의 개수가 1개 더 많아야 함.
4. X가 이겼다면 X의 개수가 O와 같아야 함.
"""
def solution(b):
    o, x = sum([arr.count('O') for arr in b]), sum([arr.count('X') for arr in b])
    #먼저 O와 X의 개수를 구해주어 1번 규칙을 통과시킴
    if 0 <= o-x <= 1:
        rb = [b[0][i]+b[1][i]+b[2][i] for i in range(3)]
        #가로는 'ooo'으로 볼 수 있지만 세로는 문자열로 확인하기 어려워서
        #가로와 세로를 바꾼 board를 reverse board의 약자인 rb로 다시 만들어줌
        # o..     ooo
        # o.. --> ...
        # o..     ...

        winO, winX = 0, 0
        # O가 이긴 경우와 X가 이긴 경우를 체크해주기 위해 변수 선언

        for i, j in zip(b, rb):
        #원래 보드판과 가로,세로를 바꾼 보드판을 묶어서 for문을 돌림
            if 'OOO' in [i,j]: winO += 1 #'OOO'가 있다면 O가 이긴횟수 1증가
            if 'XXX' in [i,j]: winX += 1 #'XXX'가 있다면 X가 이긴횟수 1증가

        diagonal = [b[0][0] + b[1][1] + b[2][2], b[0][2] + b[1][1] + b[2][0]]
        #직선으로 있는 겨우도 있지만, 대각선으로 이긴 경우도 있어서 그 경우를 넣어줌

        #대각선으로 이긴경우 더해줌
        winO += diagonal.count('OOO')
        winX += diagonal.count('XXX')

        # 둘다 이긴 경우가 있다면 0반환(2번의 경우)
        if winX and winO: return 0
        # O가 이겼는데 O의 개수가 같은 경우 0 반환(3번의 경우)
        if winO and winX == 0 and o==x: return 0
        # X가 이겼는데 O의 개수가 더 많은 경우 0 반환 (4번의 경우)
        if winX and winO == 0 and o!=x: return 0

        #나머지 경우라면 정상적인 틱택토에서 보여지는 경우라서 1반환
        return 1
        
    # O와 X의 개수가 비정상적인 경우
    return 0