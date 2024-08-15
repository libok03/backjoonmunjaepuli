# 문제
# 세로 
# R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고,
# 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 
# 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는
# 달라야 한다. 
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

# 좌측 상단에서 시작해서, 
# 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.
# 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# 입력
# 첫째 줄에 
# R과C가 빈칸을 사이에 두고 주어진다. 
# (1 ≤ R,C ≤ 20) 둘째 줄부터 
# $R$개의 줄에 걸쳐서 보드에 적혀 있는 
# $C$개의 대문자 알파벳들이 빈칸 없이 주어진다.

# 출력
# 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

import sys
input = sys.stdin.readline
from collections import deque


# 가로세로 길이 받아주기
R, C = map(int,input().split())

# 맵 만들어주고인풋 받아주기 
graph=[]
# 형식은 C길이의 str형식 R개받아주기
for _ in range(R):
    graph.append(str(input()))
    

def bfs(graph):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue = deque()
    queue.append((0,0,set(graph[0][0])))
    max_leng=0
    while queue:
        cy, cx, track = queue.popleft()
        for i in range(4):
            ax=cx+dx[i]
            ay=cy+dy[i]
            if (0<=ax<C) and (0<=ay<R):
                if graph[ay][ax] not in track: 
                    new_track = track | {graph[ay][ax]}
                    queue.append((ay,ax,new_track))
                    max_leng=max(max_leng,len(new_track))
    return max_leng

print(bfs(graph))
    
        
