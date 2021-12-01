'''
입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)
input = stdin.readline

N = int(input())

dp = [float('inf')]*(N*3)
dp[N]=0
for i in range(N-1,0,-1):
    dp[i] = min(dp[i*3],dp[i*2],dp[i+1])+1

print(dp[1])
