import sys

t = int(input()) #test case
result = ""
for i in range(t):
    # x = list(map(int,input().split())) # 기존 코드
    x = list(map(int, sys.stdin.readline().split()))
    result += str(sum(x)) + "\n"

print(result)
"""
# test case 입력
5

# 데이터 입력
1 2 3 4 5
1 2 3 4 5 6 7 8
1 2 3
1
0 0 0 1

# 출력
15
36
6
1
1
"""