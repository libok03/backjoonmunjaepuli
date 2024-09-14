# 문제
# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
# 입력
# 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다.
# C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.
# 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
# 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.
# 출력
# 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

# import 하기
import sys
input = sys.stdin.readline
# 재귀 제한 없애기
sys.setrecursionlimit(100000)

# input 받아주기
V, E = map(int, input().split())

graph=[]
for i in range(E):
    a,b,c = map(int, input().split())
    graph.append((a,b,c))
# 받은 graph cost값으로 sort해주기
graph.sort(key = lambda x: x[2])

parent = [i for i in range(V+1)]

# union - find 알고리즘 만들기
# 부모 노드 찾기
def get_parent(x):
    # 지가 그 면 그대로 리턴
    if parent[x] == x:
        return x
    # 아니면 parent[x]를 함수에 다시 넣기
    parent[x] = get_parent(parent[x])
    return parent[x]

# 부모 묶기
def union_parent(a,b):
    a= get_parent(a)
    b= get_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

answer = 0

# cost가 작은 것부터 차레대로 
for a,b,cost in graph:
    # 부모가 같지 않으면 
    if not same_parent(a,b):
        # 묶어주고 값에 더하기
        union_parent(a,b)
        answer += cost

print(answer)
