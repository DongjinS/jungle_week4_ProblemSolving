'''
입력
첫째 줄에 두 정수 N, M(0 ≤ M ≤ N-2)이 주어진다.
M은 크기가 맞지 않는, 즉 크기가 작은 돌의 개수이다.
다음 M개의 줄에는 크기가 작은 돌들의 번호가 주어진다.
1번 돌과 N번 돌은 충분히 크기가 크다고 가정한다.

출력
첫째 줄에 필요한 최소의 점프 횟수를 출력한다.
만약 N번 돌까지 점프해갈 수 없는 경우에는 -1을 출력한다.
'''
from sys import stdin
input = stdin.readline

N, M = [int(x) for x in input().split()]
#N개의 돌을 지날때 나올 수 있는 최대 속도 -- V * (V + 1) / 2 = N --WHY?? uu
VMAX = int((2 * N) ** 0.5) + 1
SMALL_STONE = set()
for _ in range(M):
    SMALL_STONE.add(int(input()))

dp = [[float("inf")]*(VMAX+1) for _ in range(N+1)]

# 2번째 돌까지는 무조건 1의 속도로 이동 회수 1회
if 2 not in SMALL_STONE:
    dp[2][1] = 1
    for cur_pos in range(3, N+1):
        if cur_pos not in SMALL_STONE:
            #현재 돌로 도달할 수 있는 모든 속도의 경우 비교
            for cur_v in range(1, int((2 * cur_pos) ** 0.5) + 1):
                dp[cur_pos][cur_v] = min(dp[cur_pos-cur_v][cur_v-1], dp[cur_pos-cur_v][cur_v], dp[cur_pos-cur_v][cur_v+1])+1
    ans = min(dp[-1])
    if ans != float('inf'):
        print(min(dp[-1]))
    else:
        print(-1)
else:
    print(-1)
