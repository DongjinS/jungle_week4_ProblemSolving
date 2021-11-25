# 1	2748	하	동적 프로그래밍	피보나치 수 2
from sys import stdin
from collections import deque
input = stdin.readline\

n = int(input())
cnt=0

q = deque()
while cnt<=n:
    if cnt == 0:
        q.append(0)
    elif cnt == 1:
        q.append(1)
    else:
        q.append(q[0]+q[1])
        q.popleft()
    cnt+=1

print(q[-1])