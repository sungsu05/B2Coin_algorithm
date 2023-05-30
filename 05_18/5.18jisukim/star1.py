# 백준
# 별찍기
import sys
input = sys.stdin.readline
for i in range(int(input())):
    print('*'*(i+1))

# 별찍기 재귀
def solution(n):
    if n <= 1:
        return n
    print("*" * solution(n - 1))
    return n

solution(int(input())+1)