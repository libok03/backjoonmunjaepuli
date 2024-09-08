#문제
#재귀적인 패턴으로 별을 찍어 보자. 
#N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
#크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
#***
#* *
#***
#N이 3보다 클 경우, 
#크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 
#예를 들어 크기 27의 패턴은 예제 출력 1과 같다.
#입력
#첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.
#출력
#첫째 줄부터 N번째 줄까지 별을 출력한다.


N = int(input())
graph=[[" "]*N for _ in range(N)]


def dp(i,j,size):
    if size ==3:
        # 사이즈가 3일때 가장 작은 단위이기 떄문에 원래대로 노출 on
        graph[i][j]="*"
        graph[i][j+1]="*"
        graph[i][j+2]="*"
        graph[i+1][j]="*"
        graph[i+1][j+2]="*"
        graph[i+2][j]="*"
        graph[i+2][j+1]="*"
        graph[i+2][j+2]="*"
    else:
        # 사이즈가 3이 아니면 가장 작은 단위가 아니기 때문에 분할해주기
        new_size=size//3
        dp(i,j,new_size)
        dp(i+new_size,j,new_size)
        dp(i+(new_size*2),j,new_size)
        dp(i,j+new_size,new_size)
        dp(i+(new_size*2), j+new_size,new_size)
        dp(i,j+(new_size*2),new_size)
        dp(i+new_size,j+(new_size*2),new_size)
        dp(i+(new_size*2),j+(new_size*2),new_size)

dp(0,0,N)
for columns in graph:
    print("".join(columns))

# 응애 DP쉬ㅇ와요
