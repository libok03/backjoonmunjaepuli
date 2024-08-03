# 11724

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는
# 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
#  (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
#  둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
#   (1 ≤ u, v ≤ N, u ≠ v)
#   같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys

input = sys.stdin.read

# 일단 정점과 간선의 개수를 받는다.
data = input().split()
N = int(data[0])
M = int(data[1])

# 리스트를 하나 만들어 그래프를 저장할 용도로 쓴다.

index=2
arr = [[] for i in range(N+1)]

# 그래프 저장 중,.
for i in range(M):
    u = int(data[index])
    v = int(data[index+1])
    arr[u].append(v)
    arr[v].append(u)
    index+=2

#이제 BFS를 이용해서 가팅 연결된 노드를 찾아보입시다.
# visited리스트를 만들어서 방문 했는지 확인

visited = [False]*(N+1)


from collections import deque

ans=0
queue = deque()

# 방문 하지 않았다면 queue에 추가후 visited에 넣고 방문했다면 continue
for i in range(1,N+1):
    if visited[i] != True:
        visited[i] = True
        queue.append(i)
        while queue:
            node= queue.popleft()
            for j in arr[node]:
                if visited[j] != True:
                    visited[j] = True
                    queue.append(j)
        ans+=1
print(ans)


# 배운점
# 1. input은 너무 느리다 sys라이브러리 stdin.read를 쓰자
# 2. 가능한 메모리를 적게 사용할 수 있도록 노력하자
