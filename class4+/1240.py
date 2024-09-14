#문제
# $N$개의 노드로 이루어진 트리가 주어지고 M개의 두 노드 쌍을 입력받을 때 두 노드 사이의 거리를 출력하라.

#입력
#첫째 줄에 노드의 개수 $N$과 거리를 알고 싶은 노드 쌍의 개수 $M$이 입력되고 다음 $N-1$개의 줄에 트리 상에 연결된 두 점과 거리를 입력받는다. 그 다음 줄에는 거리를 알고 싶은 $M$개의 노드 쌍이 한 줄에 한 쌍씩 입력된다.

#출력
# $M$개의 줄에 차례대로 입력받은 두 노드 사이의 거리를 출력한다.


import heapq
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    dv = [1e9 for _ in range(N+1)]
    dv[start]=0
    queue = [(0,start)]

    while queue:
        cnt_dist, cnt_node = heapq.heappop(queue)

        if dv[cnt_node] < cnt_dist: continue

        for adj_node, adj_dist in graph[cnt_node]:
            new_dist = cnt_dist + adj_dist
            if dv[adj_node] > new_dist:
                dv[adj_node] = new_dist
                heapq.heappush(queue,(new_dist,adj_node))
    return dv

for _ in range(M):
    a,b = map(int,input().split())
    print(dijkstra(a)[b])


