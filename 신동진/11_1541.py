'''
입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다
'''
#아이디어 - 더하기 먼저 빼기 나중에 -> 먼저 다 더해주면 큰 수를 뺄 수 있다 == 작아진다.
from sys import stdin
input = stdin.readline

calc_order = input().rstrip()
calc_order = (calc_order.split("-"))

for i in range(len(calc_order)):
    if "+" in calc_order[i]:
        calc_order[i] = sum(map(int,calc_order[i].split("+")))

res = int(calc_order[0])
for i in range(1,len(calc_order)):
    res -= int(calc_order[i])
    
print(res)