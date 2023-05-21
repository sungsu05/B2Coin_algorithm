# https://www.acmicpc.net/problem/1978
# 문제 : 소수 찾기

"""
test case

input
4
1 3 5 7

output
3
"""

def solution(x):
    if x < 2:
        return False

    for i in range(2,x):
        if x%i == 0:
            return False
        elif i * i > x + 1:
            return True
    return True

# n = int(input())
# x = list(map(int,input().split()))
n = 4
x = [1,3,5,7]
# cnt = 0
# for i in range(n):
#     if solution(x[i]):
#         cnt += 1
# print(cnt)
arr = [i for i in range(20)]
a = 2
arr.remove()