# 문제
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
# 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

# 입력
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

# 인풋 받아주기
N, B = map(int,input().split())
matrix=[]
for i in range(N):
    matrix.append(list(map(int, input().split())))

# 행렬곱 구현
def multi(A,T):
    c=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dot=0
            for k in range(N):
                # 
                dot += int(A[i][k])*int(T[k][j])
            c[i][j]=dot % 1000
    return c

def matrix_pow(matrix,power):
    result = [[1 if i ==j else 0 for j in range(N)] for i in range(N)]
    while power > 0:
        if power % 2 ==1:
            result = multi(result,matrix)
        matrix = multi(matrix,matrix)
        power //=2
    return result

ans = matrix_pow(matrix,B)

for i in ans:
    print(" ".join(map(str,i)))
########################################################
lenB=len(str(bin(B)))-3

memory=[]
if B&1:
    memory.append(matrix)
for i in range(lenB):
    matrix = multi(matrix,matrix)
    B=B>>1
    if B&1:
        memory.append(matrix)


ans=memory[0]
for i in memory[1:]:
    ans=multi(ans,i)


for i in ans:
    print(" ".join(map(str,i)))
