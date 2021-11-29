'''
문제
3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력
첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.

출력
첫째 줄에 경우의 수를 출력한다
'''
from sys import stdin
input = stdin.readline

N = int(input())
dp = [0]*(N+1)
if N>1:
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3
    for i in range(3,N+1):
        if i%2 == 0:
            sum = 0
            for j in range(i-4,-1,-2):
                sum+=dp[j]*2
            dp[i] = dp[i-2]*3+sum
print(dp[-1])