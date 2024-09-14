# 문제
# n(2 ≤ n ≤ 100)개의 도시가 있다. 
# 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
# 각 버스는 한 번 사용할 때 필요한 비용이 있다.
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다.
# 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
# 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 
# 시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

# 출력
# n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 
# 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.



import heapq

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
    for i in range(len(dv)):
        if dv[i] >= 1e9:
            dv[i] = 0
    return dv

ans = []
for i in range(1,N+1):
    ans.append(dijkstra(graph,i)[1:])

for i in ans:
    print(" ".join(map(str,i)))
