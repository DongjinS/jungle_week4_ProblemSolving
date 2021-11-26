'''
입력
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.

둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)

항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 정답은 231-1 보다 작거나 같은 자연수이다. 또한, 최악의 순서로 연산해도 연산 횟수가 231-1보다 작거나 같다.
'''
from sys import stdin
input = stdin.readline

N = int(input())

p = []
p.append(0)
for i in range(N):
    r, c = [int(x) for x in input().split()]
    if i == 0:
        p.append(r)
        p.append(c)
    else:
        p.append(c)

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N-1,0,-1):
    for j in range(i+1,N+1):
        candidate = []
        for k in range(i,j):
            candidate.append(dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1])
        if candidate:
            dp[i][j] = min(candidate)

print(dp[1][N])