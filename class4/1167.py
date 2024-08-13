# 문제
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다.
#  트리의 지름을 구하는 프로그램을 작성하시오.

# 입력
# 트리가 입력으로 주어진다.
#  먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)
#  둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 
#  정점 번호는 1부터 V까지 매겨져 있다.

# 먼저 정점 번호가 주어지고,
#  이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 
#  하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 
#  예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고,
#  정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 
#   줄의 마지막에는 -1이 입력으로 주어진다. 
#   주어지는 거리는 모두 10,000 이하의 자연수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.




import sys
input = sys.stdin.readline
from collections import deque
V= int(input())

graph =[[]for i in range(V+1)]

for _ in range(V):
    line = list(map(int,input().split()))
    cnt_node = line[0]
    idx=1
    while line[idx] != -1:
        # 내생각이랑은 다르게 따로 안하고 set에 넣어줬다.
        adj_node , adj_cost = line[idx], line[idx+1]
        graph[cnt_node].append((adj_node,adj_cost))
        idx+=2

# 내가 잘하는 BFS 구현
def BFS(start):
    q=deque()
    q.append((start,0))
    visited = [-1]*(V+1)
    visited[start] = 0
    res = [0,0]
    while q:
        cnt_node, cnt_dist = q.popleft()
        
        for adj_node, adj_dist in graph[cnt_node]:
            #방문 안했으면
            if visited[adj_node] == -1:
                #거리계산해주고
                cal_dist = cnt_dist + adj_dist
                #그만큼 queue에 append 해주고
                q.append((adj_node,cal_dist))
                visited[adj_node] = cal_dist
                # 만약 최고길이 경신하면 res에 추가
                if res[1] <cal_dist:
                    res[0] = adj_node
                    res[1] = cal_dist
    return res


# 트리 지름 공식 참고
# u-v가 지름이라고 하자. 임의의 점 x에서 가장 먼 거리의 노드 y는
# 반드시 u 또는 v이다. 따라서 y에서 BFS를
# 한번 더 해주면 지름을 구할 수 있다.
point,_ = BFS(1)
print(BFS(point)[1])

