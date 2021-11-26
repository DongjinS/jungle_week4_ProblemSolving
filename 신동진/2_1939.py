#큐 사용
from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
cnt=0

q = deque()
while cnt<=n:
    if cnt == 0:
        q.append(0)
    elif cnt == 1:
        q.append(1)
    else:
        q.append(q[0]%15746+q[1]%15746)
        q.popleft()
    cnt+=1

print(sum(q)%15746)