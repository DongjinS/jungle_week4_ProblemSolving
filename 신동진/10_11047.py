'''
입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다
'''
from sys import stdin
input = stdin.readline
N, K = [int(x) for x in input().split()]
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort()
# print(coins)
cnt = 0
cost = 0
while cost<K:
    now_coin = coins.pop()
    if now_coin<=(K-cost):
        cnt += (K-cost)//now_coin
        cost += now_coin*((K-cost)//now_coin)
        
print(cnt)