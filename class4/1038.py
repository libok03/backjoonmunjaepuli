# 문제
# 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 
# 그 수를 감소하는 수라고 한다. 
# 예를 들어, 321과 950은 감소하는 수지만, 
# 322와 958은 아니다. 
# N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 
# 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 
# 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

# 입력
# 첫째 줄에 N이 주어진다.
# N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 N번째 감소하는 수를 출력한다.
from itertools import combinations

N=int(input())

ans = []
for i in range(1,11):
    for j in combinations(range(10),i):
        num = "".join(list(map(str,reversed(list(j)))))
        ans.append(int(num))
        
ans.sort()
if N == 0:
    print(0)
elif N >= len(ans):
    print(-1)
else:
    print(ans[N]) 