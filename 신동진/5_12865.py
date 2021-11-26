'''
입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
'''
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

N, K = [int(x) for x in input().split()]

weight_values = []
#제한 중량보다 작은 중량만 포함하기.
for _ in range(N):
    w, v = [int(x) for x in input().split()]
    if w <= K:
        weight_values.append((w,v))

#dp 테이블 생성
dp = [[0]*(K+1) for _ in range(len(weight_values)+1)]

for i in range(1,len(weight_values)+1):
    for j in range(1,K+1):
        now_weight, now_value = weight_values[i-1]
        #현재 제한 무게 - j 에서 현재 물건 무게 뺀 무게에 이전 물건이 들어갈 수 있었다면
        #이전 무게가 들어갔을 당시 가치에 현재 가치 더해준게 현재 제한 무게에 들어갈 수 있다
        now_value = now_value + dp[i-1][j-now_weight]
        #현재 물건의 무게가 현재 제한 무게보다 같거나 작다면 
        if now_weight<=j:
            dp[i][j] = max(dp[i-1][j],now_value)
        #현재물건의 무게가 제한을 넘는다면 이전 물건의 가치가 그대로 내려온다.
        else:
            dp[i][j] = dp[i-1][j]
    
# print(*dp, sep="\n") 
print(dp[-1][-1])