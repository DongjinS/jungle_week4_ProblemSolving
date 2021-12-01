'''
입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 
수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.
'''
from sys import stdin
input = stdin.readline

N = int(input())
NUMS = [int(x) for x in input().split()]
dp = [0] * (N)

for i in range(N):
    dp[i] = max(dp[i-1]+NUMS[i],NUMS[i])
print(max(dp))