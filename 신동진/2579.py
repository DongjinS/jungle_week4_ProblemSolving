'''
입력
입력의 첫째 줄에 계단의 개수가 주어진다.

둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.
'''
from functools import cache
from sys import stdin
input = stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

dp = [0] * (N+1)

def FindMax(n):
    if n <= 0:
        return stairs[0]
    if n == 1:
        dp[n] = stairs[1]
        return dp[n]
    if dp[n] != 0:
        return dp[n]

    dp[n] = max(FindMax(n-3)+stairs[n-1], FindMax(n-2))+stairs[n]
    return dp[n]
    
FindMax(N)
print(dp[N])

@cache
def FindMax_cache(n):
    if n <= 0:
        return stairs[0]
    if n == 1:
        return stairs[1]
    
    return max(FindMax(n-3)+stairs[n-1], FindMax(n-2))+stairs[n]

print(FindMax(N))
