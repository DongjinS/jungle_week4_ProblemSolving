#dp 테이블 사용
from sys import stdin
input = stdin.readline

n =int(input())

dp = [0] * (n+2)
dp[1] = 1

for i in range(2,n+2):
    dp[i] = dp[i-1]%15746 + dp[i-2]%15746

print(dp[n+1]%15746)