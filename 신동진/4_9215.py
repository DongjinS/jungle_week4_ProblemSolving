'''
입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''
from sys import stdin
input = stdin.readline

#정방향: 메모리 - 36252KB 시간 - 700ms
def Rightward(string1, string2):
    dp = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]

    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
    return print(dp[-1][-1])

# 리버스: 메모리 - 36252KB 시간 - 480ms
def Reverseward(string1, string2):
    dp = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]

    for i in range(len(string1)-1,-1,-1):
        for j in range(len(string2)-1,-1,-1):
            if string1[i] == string2[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
    return print(dp[0][0])

string1 = input().strip()
string2 = input().strip()
print(string1)
print(string2)

Rightward(string1,string2)

Reverseward(string1,string2)


