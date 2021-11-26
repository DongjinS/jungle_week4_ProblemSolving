# 5	11053	상	이분 탐색	가장 긴 증가하는 부분 수열
from sys import stdin

n = int(stdin.readline())
numbers = [int(n) for n in stdin.readline().split()]
# 정렬되지 않은 상태 - 주어진 그대로 에서 가장 긴 수열을 찾아야함.

#print(n,numbers)
cnt = [1 for x in range(n)]
#print(cnt)
for i in range(n):
    for j in range(i):
        # print(f'i:{i}, j:{j}')
        #증가하면
        if numbers[i]-numbers[j]>0:
            cnt[i] = max(cnt[i],cnt[j]+1)
print(max(cnt))