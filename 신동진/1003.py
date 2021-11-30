'''
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
'''
from sys import stdin
input = stdin.readline
def fibonacci(n):
    if (n == 0):
        dp[n][0] = 1
        return dp[n]
    elif (n == 1):
        dp[n][1] = 1
        return dp[n]
    if dp[n] != [0,0]:
        return dp[n]
    else:     
        tmp1 = fibonacci(n-1)
        tmp2 = fibonacci(n-2)
        dp[n][0] = tmp1[0] + tmp2[0]
        dp[n][1] = tmp1[1] + tmp2[1]
        return dp[n]
    
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[0,0] for _ in range((N+1))]
    fibonacci(N)
    print(*dp[-1])
