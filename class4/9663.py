# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.



# N 입력 받아주기
N= int(input())

ans = 0
row = [0] * N


# 그자리에 퀸이 있는게 가능한지 판단하는 함수
def is_promising(x):
    
    for i in range(x):
        # 대각선에 퀴이 있는자, 같은 열에 퀸이 있는지
        if row[x] == row[i] or abs(row[x]-row[i])== abs(x-i):
            return False
    
    return True

# n_queen문제
def n_queens(x):
    global ans 
    # 만약 x 가 N이라면 답 +=1
    if x==N:
        ans+=1
    

    else:
        # 한 행 동안
        for i in range(N):
            # 그행의 i번째 열에 퀸을 추가하고
            row[x]=i
            # 그 퀸이 그자리에 있는게 가능하면
            if is_promising(x):
                # 다음 프로세스로 넘어가기
                n_queens(x+1)

n_queens(0)
print(ans)
