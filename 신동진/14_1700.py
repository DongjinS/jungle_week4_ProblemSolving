'''
입력
첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다.
두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다.
각 줄의 모든 정수 사이는 공백문자로 구분되어 있다. 

출력
하나씩 플러그를 빼는 최소의 횟수를 출력하시오. 
'''
from sys import stdin
from collections import deque
input = stdin.readline

N, K = [int(x) for x in input().split()]

using_order = deque([int(x) for x in input().split()])
# print(using_order)

multitap = set()
cnt=0

while using_order:
    cur_item = using_order.popleft()
    if len(multitap) != N:
        if cur_item not in multitap:
            multitap.add(cur_item)
    elif len(multitap) == N:
        if cur_item not in multitap:
            flag = 0
            for in_item in multitap:
                if in_item not in using_order:
                    multitap.remove(in_item)
                    multitap.add(cur_item)
                    flag = 1
                    cnt+=1
                    break
            if flag == 0:
                max_index = ()
                for in_item in multitap:
                    max_index = max(max_index,(using_order.index(in_item), in_item))
                multitap.remove(max_index[1])
                multitap.add(cur_item)
                cnt+=1

print(cnt)


