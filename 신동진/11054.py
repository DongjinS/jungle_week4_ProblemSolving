'''
입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
'''
from sys import stdin
input = stdin.readline

N = int(input())
seq = [int(x) for x in input().split()]

dp_inc = [1] * (N)
dp_dec = [1] * (N)
#증가하는 부분 수열
for i in range(N):
    for j in range(i):
        if seq[j]<seq[i]:
            dp_inc[i] = max(dp_inc[i],dp_inc[j]+1)

print(dp_inc)

#감소하는 부분 수열
for i in range(N-1,-1,-1):
    for j in range(i+1,N):
        if seq[j]<seq[i]:
            dp_dec[i] = max(dp_dec[i],dp_dec[j]+1)
    
print(dp_dec)
ans = 0
for i, d in zip(dp_inc, dp_dec):
    ans = max(i+d, ans)
print(ans-1)