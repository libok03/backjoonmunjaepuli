# 문제
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,
# 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.


# 입력받기
N = int(input())

# 입력 받기
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))


# 값을 받아줄 ans 설정
ans=[[0,0,0]for i in range(N)]
ans[0][0],ans[0][1],ans[0][2]=graph[0][0],graph[0][1],graph[0][2]


# 루프 동안
for i in range(1,N):
    # 이전의 내개아닌것중 가장 작은것 + 현재의 나
    ans[i][0]=min(ans[i-1][1],ans[i-1][2])+graph[i][0]
    ans[i][1]=min(ans[i-1][0],ans[i-1][2])+graph[i][1]
    ans[i][2]=min(ans[i-1][1],ans[i-1][0])+graph[i][2]

print(min(ans[N-1]))
