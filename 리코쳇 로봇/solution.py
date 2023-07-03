#문제 https://school.programmers.co.kr/learn/courses/30/lessons/169199

"""
보드 게임판의 상태를 나타내는 문자열 배열 board가 주어진다. 
로봇의 시작 위치인 "R"을 찾아서 BFS 탐색을 시작 -> BFS 탐색을 통해 로봇이 이동 가능한 위치들을 모두 방문하면서 목표 지점 "G"에 도착할 때까지 탐색
이 때, 로봇은 한 번의 이동으로 게임판 위의 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동하며, 이동 횟수를 계산합니다.

1. 게임 보드에서 로봇(R)의 위치를 찾아 큐에 추가하고, 해당 위치에서부터 BFS를 시작
2. BFS 탐색 과정에서는 현재 위치에서 네 방향으로 이동할 수 있는 경우를 찾고, 해당 방향으로 미끄러지며 이동 가능한 위치를 찾는다.
3. 이후 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우에는 큐에 해당 위치를 추가한다.
4. 만약 목표 지점(G)에 도달한 경우에는 현재까지의 이동 횟수를 반환한다.
5. BFS가 종료되었음에도 목표 지점에 도달하지 못한 경우에는 -1을 반환한다.

"""

from collections import *
dx=[-1,1,0,0]
dy=[0,0,1,-1]
 
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]
    
    # 로봇(R)의 시작 위치를 찾아 큐에 추가
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
        if q:
            break
            
    while q:
        x,y,c = q.popleft()
        
        # 목표 지점(G)에 도착한 경우 이동 횟수 반환
        if board[x][y] == 'G':
            return c
        
        # 네 방향으로 이동할 수 있는 경우 탐색
        for i in range(4):
            n_x = x
            n_y = y
            
            # 해당 방향으로 미끄러지며 이동 가능한 위치 찾기
            while 0<=n_x+dx[i]<N and 0<=n_y+dy[i]<M and board[n_x+dx[i]][n_y+dy[i]] != 'D':
                n_x += dx[i]
                n_y += dy[i]
            
            # 이전에 해당 위치에 도달한 적이 없거나, 이전에 도달한 경우보다 적은 이동 횟수로 도달 가능한 경우
            if dist[n_x][n_y] > c+1:
                dist[n_x][n_y] = c+1
                q.append((n_x,n_y,c+1))
    
    # 목표 지점에 도착할 수 없는 경우 -1 반환
    return -1