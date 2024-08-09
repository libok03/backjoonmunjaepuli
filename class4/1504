# #1054
# 문제
# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

# 출력
# 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.


import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

N,E=map(int,input().split())

graph= [[]for i in range(N+1)]
for i in range(E):
    node1,node2,leng=map(int,input().split())
    graph[node1].append((node2,leng))
    graph[node2].append((node1,leng))


def daykstra(start):
    # 거리 저장용
    dv=[INF] * (N+1)
    dv[start]=0
    # 우선순이 큐를 이용하여 (0,start)저장
    priority_queue = [(0,start)]
    # 우선순위 큐에서
    while priority_queue:
        # 가장 작은 수의 dist를 가지는 노드를 꺼내 와서
        curr_dist, curr_node = heapq.heappop(priority_queue)
        # 그 길이가 새로 만든 길이보다 작다면
        if curr_dist > dv[curr_node]:
            continue

        # 그 노드의 이어진 그래프에서
        for adj_node,adj_dist in graph[curr_node]:
            distance = curr_dist + adj_dist
            # 새로 구한 거리가 더 작다면
            if distance < dv[adj_node]:
                # 바꿔주고
                dv[adj_node] = distance
                # 우선 순위 큐에 집어넣기
                heapq.heappush(priority_queue,(distance,adj_node))
    return dv

v1,v2 = map(int,input().split())

origin_dist= daykstra(1)
v1_dist=daykstra(v1)
v2_dist=daykstra(v2)
result = min((origin_dist[v1]+v1_dist[v2]+v2_dist[N]),(origin_dist[v2]+v2_dist[v1]+v1_dist[N]))
print(result if result < INF else -1)

# 기존의 BFS로 풀었었는데 이 경우에는 방문 여부와 루트와 가까운 거리를 따로 찾아야 한다는 단점이 있었지만, 
# 우선순위 큐를 사용 하니 덩ㄱ 쉽게 풀렸다.

