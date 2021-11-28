'''
입력
첫째 줄에 도시의 수 N이 주어진다.
(2 ≤ N ≤ 16) 다음 N개의 줄에는 비용 행렬이 주어진다.
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.

항상 순회할 수 있는 경우만 입력으로 주어진다.

출력
첫째 줄에 외판원의 순회에 필요한 최소 비용을 출력한다.
'''
from sys import stdin
input = stdin.readline

N = int(input())
city_map = []
for _ in range(N):
    tmp = [int(x) for x in input().split()]
    city_map.append(tmp)

#모든 방문에 대한 비트 켜져 있는 상태 - VISITED_ALL
VISITED_ALL = (1 << N) -1
# 방문 상태(지나온 도시) 저장 - 비트 방식으로  0 = 0000 1 = 0001 2 = 0010
# 시작할때는 0번째 도시에서 부터 시작하므로 0번째 도시의 비트를 키고 들어간다. 1 << 0 = 1 = 0001
visited = 1
#dp 테이블 생성 - 캐쉬역활
dp_table = [[None]*(1<<N) for _ in range(N)]

def FindPath(city_map, cur_start, visited):
    #끝에 왔으면 마지막 돌아가는 거리 반환, 연결안되어 있으면 inf 반환
    if visited == VISITED_ALL:
        return city_map[cur_start][0] or float('inf')
    #이미 경로 탐색을 했던 곳이면 저장해 두었던 최솟값 반환 
    # - e.g. 12431, 12341를 이미 탐색해서 12까지 왔을 때 12이후의 최솟값이 이미 저장되어 있다면 바로 반환
    if dp_table[cur_start][visited] != None:
        return dp_table[cur_start][visited]
    
    tmp_min = float('inf')
    for city in range(len(city_map[cur_start])):
        # visited 는 0(맨 오른쪽)에서 부터 켜지기 때문에 
        # & 연산에서 새로운 도시에 대해서는 0을 반환 하고 이미 왔던 도시는 이미 왔던 도시의 비트 값을 반환한다.
        # 0 이면 아직 방문하지 않은 도시라는 뜻
        if visited & (1<<city) == 0 and city_map[cur_start][city] != 0:
            #visited|1<<city , |(=or) 연산을 통해서 visited 에 방문할(탐색할) city를 포함시킨다.
            #거리를 비교할때 현재 도시에서 탐색할 도시의 거리를 탐색의 반환 값에 더해준다
            tmp_min = min(tmp_min, FindPath(city_map, city, visited|1<<city) + city_map[cur_start][city])
    dp_table[cur_start][visited] = tmp_min
    return tmp_min

#처음 부른 함수의 리턴 = 마지막으로 반환되는 tmp_min 값이 시작점에서부터 모든 도시를 돌아 시작점으로 돌아오는 최소값
FindPath(city_map,0,visited)
print(dp_table[0][1])

