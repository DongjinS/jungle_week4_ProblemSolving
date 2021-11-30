'''
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''
from sys import stdin, setrecursionlimit
from functools import cache
input = stdin.readline
setrecursionlimit(10**8)

N = int(input())
color_price = []
for i in range(N):
    color_price.append([int(x) for x in input().split()])

dp = [[None] * 3 for _ in range(N)]


def FindMin(cur_house,color):
    if color < 0 or color > 2:
        return float('inf')

    if cur_house == N-1:
        return color_price[cur_house][color]

    if dp[cur_house][color] != None:
        return dp[cur_house][color]
    
    for cur_color in range(3):
        #미스테리..
        candidate = [FindMin(cur_house+1,cur_color-1),FindMin(cur_house+1,cur_color+1), FindMin(cur_house+1,cur_color+2), FindMin(cur_house+1,cur_color-2)]
        print(*dp, sep="\n")
        dp[cur_house][cur_color] = min(FindMin(cur_house+1,cur_color-1),FindMin(cur_house+1,cur_color+1), FindMin(cur_house+1,cur_color+2), FindMin(cur_house+1,cur_color-2)) + color_price[cur_house][cur_color]
    return dp[cur_house][cur_color]

FindMin(0,0)
print(*dp, sep="\n")
print(min(dp[0]))