# 콜랩 국룰
import sys
input=sys.stdin.readline

# 우선순위 큐 불러와주기
import heapq

# 데이터 받아주기
N=int(input())
M=int(input())

graph=[[] for i in range(N+1)]

for i in range(M):
    node1,node2,cost=map(int,input().split())
    graph[node1].append((node2,cost))

# 다익스트라 구현
def dijkstra(start):
    # dv에 거리, 그동안 거쳐온 노드 저장 
    dv=[[1e9,[]] for _ in range(N+1)]
    dv[start][0]=0
    # 우선 순위 큐 설정
    q= [(0,start,[start])]

    # 루프 on
    while q:
        # 뽑아주고
        cnt_cost, cnt_node, cnt_root= heapq.heappop(q)

        # 만약 dv가 더 작으면 패스
        if dv[cnt_node][0] < cnt_cost:
            continue

        # 아니면 인접노드 싹다 불러와서 
        for adj_node, adj_cost in graph[cnt_node]:
            # 새 비용, 루트 그해주고
            wholecost=cnt_cost+adj_cost
            new_root=cnt_root+[adj_node]

            # 만약 dv보다 적으면 바꿔주기
            if dv[adj_node][0]>wholecost:
                 dv[adj_node][0]=wholecost
                 dv[adj_node][1]=new_root
                 # 마지막으로 푸쉬
                 heapq.heappush(q,(wholecost,adj_node,new_root))
    return dv

A,B=map(int,input().split())


ans= dijkstra(A)
# 최소비용 출력
print(ans[B][0])
# 거쳐온 노드 개수 출력
print(len(ans[B][1]))
# 거쳐온 노드 출력
for i in ans[B][1]:
    print(i, end=" ")
