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
SMALL_STONES = set()
for _ in range(M):
    SMALL_STONES.add(int(input()))
VMAX = int((2*N)**0.5) + 1

dp_table = [[float('inf')]*(VMAX+1) for _ in range(N+1)]

for now_stone in range(2,N+1):
    if now_stone not in SMALL_STONES:
        if now_stone == 2:
            dp_table[now_stone][1] = 1
        else:
            for now_V in range(1, int((2*now_stone)**0.5) + 1):
                dp_table[now_stone][now_V] = min(dp_table[now_stone-now_V][now_V-1], dp_table[now_stone-now_V][now_V], dp_table[now_stone-now_V][now_V+1]) + 1

ans = min(dp_table[-1])
if ans != float('inf'):
    print(ans)
else:
    print(-1)