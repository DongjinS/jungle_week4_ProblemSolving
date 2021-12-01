'''
입력
첫째 줄에 포도주 잔의 개수 n이 주어진다.
(1 ≤ n ≤ 10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

출력
첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.
'''
from sys import stdin
input = stdin.readline

N = int(input())
wine = [0]
for _ in range(N):
    wine.append(int(input()))

dp = [0] * (N+1)
if N>2:
    dp[1] = wine[1]
    for i in range(1,N+1):
        dp[i] = max(dp[i-2], dp[i-3]+wine[i-1])+wine[i]
        #두번 연속 안먹을 경우를 고려하기 위해서.. 이해 잘 안감
        dp[i] = max(dp[i-1],dp[i])
        # print(dp)
    print(max(dp))
else:
    print(sum(wine))