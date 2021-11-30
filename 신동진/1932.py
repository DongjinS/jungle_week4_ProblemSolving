'''
입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
'''
from sys import stdin
input = stdin.readline

N = int(input())

tree = []
for _ in range(N):
    tree.append([int(x) for x in stdin.readline().split()])

# print(*tree, sep="\n")
for i in range(len(tree)):
    if i==1:
        tree[i][0] = tree[i][0] + tree[0][0]
        tree[i][1] = tree[i][1] + tree[0][0]
    if i>1:
        for j in range(len(tree[i])):
            if j==0:
                tree[i][j] = tree[i][j] + tree[i-1][0]
            elif j==len(tree[i])-1:
                tree[i][j] = tree[i][j] + tree[i-1][j-1]
            else:
                tree[i][j] = max(tree[i][j] + tree[i-1][j-1], tree[i][j] + tree[i-1][j])

# print(*tree, sep="\n")
print(max(tree[-1]))
