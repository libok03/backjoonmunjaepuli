# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
#  단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. 
#  (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
#   모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
#  둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
#  셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
#  이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
#  서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, 
# i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 
# 시작점 자신은 0으로 출력하고, 
# 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.


#우선 순위 큐
import heapq
#백준 필수 임포트
import sys
input = sys.stdin.readline

# 입력 받기
V,E= map(int, input().split())

start=int(input())

graph= [[]for i in range(V+1)]


for i in range(E):
    node1,node2,leng= map(int,input().split())
    graph[node1].append((node2,leng))


# 데이크스트라 알고리즘
def daykstra(start):
    dv=[1e9]*(V+1)
    dv[start]=0
    # 시작점 지정
    q=[(0,start)]

    
    while q:
        #q에서 현재 노드, 거리 뽑아오기
        cnt_dist, cnt_node = heapq.heappop(q)

        # 만약 현재 뽑아온 거리가 dv저장 거리와 다르면 안함
        if cnt_dist > dv[cnt_node]:
            continue

        # 인접 노드 확인해서
        for adj_node, adj_dist in graph[cnt_node]:
            # 만약 거리가 더 적으면
            if dv[adj_node] > adj_dist+cnt_dist:
                # 바꿔주고
                dv[adj_node] = adj_dist+cnt_dist
                # q에 저장!
                heapq.heappush(q,(adj_dist+cnt_dist , adj_node))

    return dv


for i in daykstra(start)[1:V+1]:
    print(i if  i < 1e9 else "INF")
