'''
문제
2×N 크기의 벽을 2×1, 1×2, 1×1 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.
'''
from sys import stdin
input = stdin.readline
MOD = 1000000007
N = int(input())
dp = [0]* (N+1)
dp_for_sum = [0]* (N+1)
if N>0:
    for i in range(N+1):
        if i == 0:
            dp[0]=1
        else:
            if dp_for_sum[i-1] == 0:
                for j in range(i-3,-1,-1):                                                                          
                    dp_for_sum[i]+=dp[j]*2
            else:
                dp_for_sum[i] = dp_for_sum[i-1]+dp[i-3]*2
            dp[i] = (dp[i-1]*2 + dp[i-2]*3 + dp_for_sum[i])%MOD

print(dp[N]%MOD)