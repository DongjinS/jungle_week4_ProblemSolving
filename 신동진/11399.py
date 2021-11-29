'''
입력
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
'''
from sys import stdin
input = stdin.readline

N = int(input())
time_required = [int(x) for x in input().split()]

# print(time_required)
time_required.sort()
ans = 0
for i in range(1,N):
    time_required[i] += time_required[i-1]

print(sum(time_required))
