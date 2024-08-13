
#1043

# 입력
# 첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.
# 둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고
#  그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.
# 셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.
# N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수,
#  파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.
# import sys
# input = sys.stdin.readline

#find_parent함수를 통해서 부모 노드를 찾아준다.
def find_parent(x):
    if parents[x]!=x:
        parents[x] =find_parent(parents[x])
    return parents[x]

#union 함수를 통해서 노드끼리 묶어준다(간선을 만들어준다!).
def union(a,b):
    if a<b:
        parents[b]=a
    else:
        parents[a]=b


# 인풋을 받아준다.
N,M=map(int,input().split())

knower=set(list(map(int,input().split()))[1:])

parents=list(range(N+1))

graph=[]
for i in range(M):
    data=list(map(int,input().split()))[1:]
    graph.append(data)

# union함수를 통해서 노드끼리 간선을 만들어준다.
for i in graph:
    for j in i:
        union(i[0],j)


#knower의 부모노드를 저장한다.
knower_parents=set()
for i in knower:
    knower_parents.add(find_parent(i))

#정잡 구하기!
cnt=M
for i in graph:
    temp=1
    for j in i:
        if find_parent(j) in knower_parents:
            temp=0
    if temp==0:
        cnt-=1


print(cnt)


#아니 다중 union함수를 찾아봐야겠다 너무 번거롭다.



# 번외
import sys
input= sys.stdin.readline


N,M= map(int, input().split())
data =list(map(int,input().split()))
knower = set(data[1:])
graph=[]
for i in range(M):
    data=list(map(int,input().split()))
    graph.append(set(data[1:]))

for k in range(M):
    for i in graph:
        if len(i & knower) >=1:
            for j in i:
                knower.add(j)




cnt=0
for i in graph:
    if len(i & knower) >= 1:
        continue
    else:
        cnt+=1
print(cnt)

#아니 그냥 처음 낸거에  M번 반복하면 그게 정답이었다.
#나는 병신이다.
