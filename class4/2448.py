n = int(input())

pic=  [[" "]*2*n for i in range(n)]

size=n

def recursion(i,j,size):
    if size == 3:
        pic[i][j]="*"
        pic[i+1][j-1]=pic[i+1][j+1]="*"
        for k in range(-2,3):
            pic[i+2][j-k]="*"
    
    else:
        new_size=int(size/2)
        recursion(i,j,size/2)
        recursion(i+new_size,j+new_size,size/2)
        recursion(i+new_size,j-new_size,size/2)

recursion(0,n-1,n)
for i in pic:
    for j in i:
        print(j,end="")
    print()
