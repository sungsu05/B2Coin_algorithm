# https://www.acmicpc.net/problem/2439
# 문제 : 별찍기
def solution(n,x):
    if n<=1:
        return n
    solution(n - 1,x)
    # print(n)
    # print(n-1,x-n)
    print((x-n) * " " + (n-1) * "*")
    return n

"""
입력값 5 + 1 , 6이라 가정
i = 1 , n = 6
i = 2 , n = 5
i = 3 , n = 4
i = 4 , n = 3
i = 5 , n = 2 << 재귀 시작

재귀 시작, x의 고정값은 항상 n(6)
i = 5   n = 2    n-1 = 1    x - n = 4
i = 4   n = 3    n-1 = 2    x - n = 3
i = 3   n = 4    n-1 = 3    x - n = 2
i = 2   n = 5    n-1 = 4    x - n = 1
i = 1   n = 6    n-1 = 5    x - n = 0
"""
# n = int(input()) +1
# solution(n,n)


# (n := int(input()))
n = 5
print("".join([(n-i)*' '+(i*'*')+'\n' for i in range(1,n+1)]))
