#동전
'''
입력
입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 동전의 가지 수 N(1 ≤ N ≤ 20)이 주어지고 두 번째 줄에는 N가지 동전의 각 금액이 오름차순으로 정렬되어 주어진다.
각 금액은 정수로서 1원부터 10000원까지 있을 수 있으며 공백으로 구분된다. 세 번째 줄에는 주어진 N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)이 주어진다.

편의를 위해 방법의 수는 231 - 1 보다 작고, 같은 동전이 여러 번 주어지는 경우는 없다.

출력
각 테스트 케이스에 대해 입력으로 주어지는 N가지 동전으로 금액 M을 만드는 모든 방법의 수를 한 줄에 하나씩 출력한다.
'''
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = [int(x) for x in input().split()]
    target = int(input())

    dp = [0] * (target+1)
    for coin in coins:
        for i in range(coin,len(dp)):
            if i-coin == 0:
                dp[i] = dp[i] + 1 
            elif dp[i-coin] != 0:
                #이전꺼에 '잘!' 누적하기..
                dp[i] = dp[i] + dp[i-coin]
    print(dp[target])

