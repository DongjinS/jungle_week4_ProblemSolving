'''
입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''
from sys import stdin
input= stdin.readline
MOD = 1000000000
N = int(input())

dp = [[1] * 10 for _ in range(N+1)]
for i in range(2,N+1):
    for n in range(10):
        if n == 0:
            dp[i][n] = dp[i-1][n+1]%MOD
        elif n == 9:
            dp[i][n] = dp[i-1][n-1]%MOD
        else:
            dp[i][n] = dp[i-1][n-1]%MOD + dp[i-1][n+1]%MOD

print(sum(dp[N][1:])%MOD)
