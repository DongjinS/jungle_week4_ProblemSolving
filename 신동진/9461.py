'''
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

출력
각 테스트 케이스마다 P(N)을 출력한다.
'''
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,N):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[N-1])