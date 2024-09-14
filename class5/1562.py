# 문제
# 45656이란 수를 보자.

# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

# N이 주어질 때, 
# 길이가 N이면서 0부터 9까지 숫자가 모두 등장하는 계단 수가 
# 총 몇 개 있는지 구하는 프로그램을 작성하시오. 
# 0으로 시작하는 수는 계단수가 아니다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.


N = int(input())

# 3차원 배열 선언 (N*10*1024)
dp = [[[0 for _ in range(1<<10)]for _ in range(10)] for _ in range(N)]

mod = 1000000000
res=0

# 10 동안
for k in range(1,10):
    # 시작 부분을 1로 설정
    dp[0][k][1<<k] = 1

# N 동안
for i in range(1,N):
    # 10개 를 탐색하는데
    for k in range(10):
        # 1024개를 돌아보면서
        for bit in range(1024):
            # 만약 k가 1이상이면 (0이 아니라면)
            if k-1 >= 0 :
                # 이전 값에서 bit영역에 수 추가하기
                dp[i][k][bit | (1<<k)] += dp[i-1][k-1][bit]
            # 만약 k가 8이하라면 (9가 아니라면)
            if k+1 <= 9:
                # 이전 값에서 bit영역에 수 추가하기
                dp[i][k][bit | (1<<k)] += dp[i-1][k+1][bit]
            #mod로 나눈 나머지값
            dp[i][k][bit | (1<<k)] %= mod


# 자 이러면 1023부분만 확인하면 됩니다. 
for k in range(10):
    res+= dp[N-1][k][1023]
    res%=mod

print(res)

# 비트필드를 처음 써봤는데 새롭다.
# 아직 길은 멀구나...
