'''
입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

제한
-50 ≤ a, b, c ≤ 50
'''
from sys import stdin
input = stdin.readline
from collections import defaultdict
def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    if dp[(a,b,c)]:
        return dp[(a,b,c)]
    if a < b and b < c:
        dp[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[(a,b,c)]
    else:
        dp[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[(a,b,c)]

dp = defaultdict(int)
a = 0
b = 0
c = 0
while a!=-1 or b!=-1 or c!=-1:
    a,b,c = [int(x) for x in input().split()]
    if a!=-1 or b!=-1 or c!=-1:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
