# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/86052

# 재귀 호출의 최대 깊이를 설정하는 부분
import sys
sys.setrecursionlimit(500000)

# 로봇의 이동 방향을 상수로 정의 (0:북, 1:동, 2:남, 3:서)
DIR = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
answer = []  # 가능한 모든 경로의 이동 횟수를 저장할 리스트

def calMove(x, y, n, m):
    # 그리드를 넘어갈 때 새로운 위치를 계산하는 함수
    return (x % n, y % m)

def calDir(cur, d):
    # 현재 방향과 회전 방향을 고려하여 새로운 방향을 계산하는 함수
    if cur == 'S':
        return d
    elif cur == 'R':
        return (d + 1) % 4
    else:
        return (d - 1) % 4

def search(tx, ty, td, x, y, d, visited, grid, count):
    # 백트래킹을 이용하여 가능한 모든 경로를 탐색하는 함수
    n, m = len(grid), len(grid[0])
    visited[(x, y, d)] = True  # 현재 위치와 방향을 방문한 것으로 표시
    count += 1  # 이동 횟수 증가
    dx, dy = DIR[d]
    x, y = calMove(x + dx, y + dy, n, m)  # 새로운 위치 계산
    d = calDir(grid[x][y], d)  # 새로운 방향 계산
    if (x, y, d) == (tx, ty, td):  # 목표 위치에 도달한 경우
        answer.append(count)  # 이동 횟수를 저장
        return
    elif (x, y, d) in visited:  # 이미 방문한 경우
        return
    else:
        search(tx, ty, td, x, y, d, visited, grid, count)  # 재귀적으로 탐색
        return

def solution(grid):
    n, m = len(grid), len(grid[0])
    visited = {}  # 이미 방문한 위치와 방향을 저장하는 딕셔너리
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if (i, j, d) not in visited:  # 아직 방문하지 않은 경우
                    search(i, j, d, i, j, d, visited, grid, 0)  # 탐색 시작

    answer.sort()  # 결과 정렬
    return answer  # 가능한 모든 경로의 이동 횟수 반환
