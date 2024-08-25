# 문제
# n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
# 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 
# 항상 시작점에서 도착점으로의 경로가 존재한다.

# 입력
# 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 
# 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
# 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 
# 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
# 그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
# 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다.
# 출발 도시와 도착 도시도 포함한다.
# 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.


# 우선 순위 큐 임포트
import heapq
import sys
input = sys.stdin.readline

# 입력 값 받아주기
N = int(input())
M=int(input())
graph = [[] for i in range(N+1)]

for i in range(M):
    par_node,son_node,leng= map(int,input().split())
    graph[par_node].append((son_node,leng))

# 다익스트라 알고리즘
def dijkstra(graph,start):
  # dv, queue 만들어주고
    dv=[1e9 for _ in range(N+1)]
    queue=[(0, start)]
    # 시작 부분 거리 0으로 설정
    dv[start]=0
    # queue가 존재하는 동안
    while queue:
        # queue 에서 꺼내와서
        cnt_leng, cnt_node = heapq.heappop(queue)
        # 만약 dv가 더 크면 continue
        if dv[cnt_node] < cnt_leng: continue
        # 아니면 계산
        for adj_node, adj_leng in graph[cnt_node]:
            new_leng= cnt_leng+ adj_leng
            # 계산 값이 더 작으면
            if dv[adj_node] > new_leng:
                # 바꿔주고
                dv[adj_node]= new_leng
               # queue에 추가
                heapq.heappush(queue,(new_leng,adj_node))
    return dv

start,end = map(int, input().split())

ans=dijkstra(graph,start)[end]

print(ans)
