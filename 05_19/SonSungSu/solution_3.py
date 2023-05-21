# https://www.acmicpc.net/problem/20492
# 문제 : 세금
def solution(x):
    operaotr = [
        lambda x: x-x*0.22,
        lambda x:x - (x*0.2)*0.22
    ]
    result = " ".join([str(int(operaotr[i](x))) for i in range(len(operaotr))])
    return result


print(solution(int(input())))
# x = int(input())
# print(int(x - (x*0.22)),int(x - (x*0.2)*0.22))
