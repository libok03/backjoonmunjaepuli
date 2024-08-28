# 문제
# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 
# 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 
# 가방에는 최대 한 개의 보석만 넣을 수 있다.
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 C가 주어진다. (1 ≤ Ci ≤ 100,000,000)
# 모든 숫자는 양의 정수이다.
# 출력
# 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

import heapq
import sys
input = sys.stdin.readline

# 인풋 받아주기
n,k = map(int,input().split())

gems = [[*map(int, input().split())]for _ in range(n)]

bags = [int(input()) for _ in range(k)]
# 오름차순으로 정렬
gems.sort() ; bags.sort()

result = 0 ; tmp = []

# 하나의 가방당 (작은 거 부터)
for bag in bags:
    # 만약 가방에 존재하는 보석이 담기면
    while gems and gems[0][0] <=bag:
        # tmp에 그 보석의 가격을 넣어주고
        heapq.heappush(tmp, -gems[0][1])
        # 그 보석 뽑기
        heapq.heappop(gems)

    # tmp가 존재하면
    if tmp:
        # tmp중에 가장 큰 숫자 pop해서 더하기
        result-= heapq.heappop(tmp)

print(result)
