'''
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''
#피보나치 수열 동일
from sys import stdin
input = stdin.readline
from collections import deque
MOD = 10007
N = int(input())
#메모리 29200  시간 68
def dp_table(N):
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    # print(dp)
    for i in range(2,N+1):
        dp[i] = dp[i-1]%MOD + dp[i-2]%MOD

    print(dp[N]%MOD)
#메모리 32696  시간 92
def que(N,MOD):
    q = deque([1,1])
    for i in range(2,N+1):
        q.append(sum(q)%MOD)
        q.popleft()
    print(q[-1]%MOD)

dp_table(N)
que(N,MOD)