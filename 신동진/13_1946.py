'''
입력
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다.
각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다.
두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

출력
각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.
'''
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    recruitment = []
    for _ in range(N):
        D, I = [int(x) for x in input().split()]
        recruitment.append((D,I))
    recruitment.sort()
    print(recruitment)
    ans = [recruitment[0]]
    for i in range(1, len(recruitment)):
        if recruitment[i][1] < ans[-1][1]:
            ans.append(recruitment[i])
    print(ans)
    print(len(ans))