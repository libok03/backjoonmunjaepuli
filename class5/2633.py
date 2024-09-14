# 인터넷 방송 KOI(Korea Open Internet)의 음악 프로그램 PD인 남일이는 자기가 맡은 프로그램
# '뮤직 KOI'에서 가수의 출연 순서를 정하는 일을 매우 골치 아파한다. 
# 순서를 정하기 위해서는 많은 조건을 따져야 한다.
# 그래서 오늘 출연 예정인 여섯 팀의 가수에 대해서 남일이가 보조 PD 세 명에게 각자 담당한 가수의 출연 순서를 정해오게 하였다. 
# 보조 PD들이 가져온 것은 아래와 같다.
# 1 4 3
# 6 2 5 4
# 2 3
# 첫 번째 보조 PD는 1번 가수가 먼저, 다음에 4번 가수, 다음에 3번 가수가 출연하기로 순서를 정했다. 
# 두 번째 보조 PD는 6번, 2번, 5번, 4번 순으로 자기 담당 가수들의 순서를 정했다. 
# 한 가수를 여러 보조 PD가 담당할 수도 있다. 마지막으로, 세 번째 보조 PD는 2번 먼저, 다음에 3번으로 정했다.
# 남일이가 할 일은 이 순서들을 모아서 전체 가수의 순서를 정하는 것이다. 
# 남일이는 잠시 생각을 하더니 6 2 1 5 4 3으로 순서를 정했다. 
# 이렇게 가수 순서를 정하면 세 보조 PD가 정해온 순서를 모두 만족한다. 
# 물론, 1 6 2 5 4 3으로 전체 순서를 정해도 괜찮다.
# 경우에 따라서 남일이가 모두를 만족하는 순서를 정하는 것이 불가능할 수도 있다.
# 예를 들어, 세 번째 보조 PD가 순서를 2 3 대신에 3 2로 정해오면 남일이가 전체 순서를 정하는 것이 불가능하다. 
# 이번에 남일이는 우리 나라의 월드컵 4강 진출 기념 음악제의 PD를 맡게 되었는데, 출연 가수가 아주 많다. 
# 이제 여러분이 해야 할 일은 보조 PD들이 가져 온 순서들을 보고 남일이가 가수 출연 순서를 정할 수 있도록 도와 주는 일이다.
# 보조 PD들이 만든 순서들이 입력으로 주어질 때, 전체 가수의 순서를 정하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 가수의 수 N과 보조 PD의 수 M이 주어진다. 가수는 번호 1, 2,…,N 으로 표시한다.
# 둘째 줄부터 각 보조 PD가 정한 순서들이 한 줄에 하나씩 나온다. 각 줄의 맨 앞에는 보조 PD가 담당한 가수의 수가 나오고, 
# 그 뒤로는 그 가수들의 순서가 나온다. N은 1이상 1,000이하의 정수이고, M은 1이상 100이하의 정수이다.
# 출력
# 출력은 N 개의 줄로 이뤄지며, 한 줄에 하나의 번호를 출력한 다. 
# 이들은 남일이가 정한 가수들의 출연 순서를 나타낸다. 답이 여럿일 경우에는 아무거나 하나를 출력 한다. 
# 만약 남일이가 순서를 정하는 것이 불가능할 경우에는 첫째 줄에 0을 출력한다.

# 덱 import
from collections import deque
import sys
input = sys.stdin.readline

# 인풋 받아주기
N, M = map(int,input().split())
data=[]
graph = [[] for _ in range(N+1)]
singers = [0 for i in range(N+1)]
for i in range(M):
    data.append(list(map(int, input().split()))[1:])

# singers에서는 노드가 몇개 연경 되어있는지, graph에는 앞에 뭐가 더있는지 연결해주는 역할
for i in data:
    for j in range(len(i)-1):
        singers[i[j+1]] += 1
        graph[i[j]].append(i[j+1])

# 큐를 만들어 주고
queue = deque()

for i in range(1,N+1):
    if singers[i] == 0:
        queue.append(i)


ans=[]
# 큐를 돌리는 동안
while queue:
    cnt_singer = queue.popleft()
    # 답에 pop한걸 추가해주고
    ans.append(cnt_singer)
    # graph에서 가져온 앞의 노드를 singers에서 1씩 빼주고
    for i in graph[cnt_singer]:
        singers[i] -= 1
        if singers[i] == 0:
            # 만약 0 이면 append
            queue.append(i)

# 아래는 모두 다 불렀는지 조새해서
ans_point= True
for i in singers:
    if i > 0:
        ans_point = False

if ans_point:
    for i in ans:
        print(i)
else:
    # 아니면 0 출력
    print(0)
