# https://www.acmicpc.net/problem/25192
# 문제 : 곰곰 이모티콘

import sys
t = int(input())

arr = []
cnt = 0

#  시간 초과
# for i in range(t):
#     str = sys.stdin.readline()
#     if str == "ENTER\n":
#         arr = []
#     elif arr.count(str):
#         continue
#     else:
#         cnt += 1
#         arr.append(str)

for i in range(t):
    str = sys.stdin.readline()
    if str == "ENTER\n":
        cnt += len(set(arr))
        arr = []
    else:
        arr.append(str)

print(cnt + len(set(arr)))