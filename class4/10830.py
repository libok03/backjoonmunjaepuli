N, B = map(int,input().split())
matrix=[]
for i in range(N):
    matrix.append(list(map(int, input().split())))

ans= list()

def multi(A,T):
    c=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dot=0
            for k in range(N):
                dot += int(A[i][k])*int(T[k][j])
            c[i][j]=dot % 1000
    return c

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
