# 2166

# 문제
# 2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 
# 이 다각형의 면적을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N이 주어진다. 
# 다음 N개의 줄에는 다각형을 이루는 순서대로 N개의 점의 x, y좌표가 주어진다. 
# 좌표값은 절댓값이 100,000을 넘지 않는 정수이다.

# 출력
# 첫째 줄에 면적을 출력한다. 
# 면적을 출력할 때에는 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력한다.

################
#   처음 풀이   #
################

import math
N = int(input())

graph=[]
all_a = 0
all_b = 0
for i in range(N):
    a,b = map(int,input().split())
    graph.append((a,b))
    all_a+=a
    all_b+=b
    
all_a /= N
all_b /= N


ans = 0
for i in range(N-1):
    x1,y1 = graph[i][0], graph[i][1]
    x2,y2 = graph[i+1][0], graph[i+1][1]
    if x1 != x2:
        ans += abs((math.sqrt(((x1-x2)**2)+((y1-y2)**2))) * (((((y1-y2)/(x1-x2)) * (all_a - x1)) + y2 - all_b) / (math.sqrt((((y1-y2)/(x1-x2))**2)+1))) /2)
    else:
        ans += abs((math.sqrt(((x1-x2)**2)+((y1-y2)**2))) * (all_a - x1) /2)
    
x1,y1 = graph[0][0], graph[0][1]
x2,y2 = graph[N-1][0], graph[N-1][1]
if x1 != x2:
        ans += abs((math.sqrt(((x1-x2)**2)+((y1-y2)**2))) * (((((y1-y2)/(x1-x2)) * (all_a - x1)) + y2 - all_b) / (math.sqrt((((y1-y2)/(x1-x2))**2)+1))) /2)
else:
    ans += abs((math.sqrt(((x1-x2)**2)+((y1-y2)**2))) * (all_a - x1) /2)

print(round(ans,1))



################
#   다음 풀이   #
################


import sys
input = sys.stdin.readline

N = int(input())

graph=[]
for i in range(N):
    graph.append(list(map(int,input().split(" "))))
graph.append(graph[0])
ans = 0
for i in range(N):
    ans += graph[i][0]*graph[i+1][1] - graph[i+1][0]*graph[i][1]
    

print(round((abs(ans)/2),1))


