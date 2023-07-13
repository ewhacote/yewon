#문제 https://school.programmers.co.kr/learn/courses/30/lessons/154540

"""
기본적인 탐색 문제. 무인도를 만나면 무인도 전체를 탐색하며(BFS, DFS 상관 없음) 인접한 모든 무인도를 방문하고, 방문한 무인도의 합을 result에 삽입한다. 나중에 result를 검사하여 빈 리스트라면 [-1]를 반환, 그렇지 않으면 정렬 후 반환하면 끝
"""

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    M, N = len(maps), len(maps[0])
    visited = [[False]*N for _ in range(M)]
    
    answer = []
    
    for i in range(M) :
        for j in range(N) :
            if maps[i][j] != "X" and not visited[i][j] :
                period = 0
                q = [(j, i)]
                
                while q :
                    x, y = q.pop()
                    if visited[y][x] :
                        continue
                    visited[y][x] = True
                    period += int(maps[y][x])
                    
                    for k in range(4) :
                        ax, ay = x + dx[k], y + dy[k]
                        if -1 < ax < N and -1 < ay < M and maps[ay][ax] != "X" and not visited[ay][ax] :
                            q.append((ax, ay))
                    
                answer.append(period)
    
    return sorted(answer) if answer else [-1]