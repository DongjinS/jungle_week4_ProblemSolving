'''
문제
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×17 직사각형을 채운 한가지 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''
from sys import stdin
input = stdin.readline
MOD = 10007
N = int(input())
dp = [1] * (N)
for i in range(1,N):
    dp[i] = dp[i-1]%MOD + (dp[i-2]*2)%MOD

print(dp[-1]%MOD)