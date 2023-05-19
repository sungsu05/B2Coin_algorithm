# 백준 별찍기2
import sys
input = sys.stdin.readline
n = int(input())

# sol1 그냥 풀어보기
for i in range(1, n+1):
    print(' '*(n-i)+'*'*i)

# sol2 오른쪽 정렬
for i in range(n):
    star = '*'*(i+1)
    print(star.rjust(n))
# 전체 n에서 오른쪽 정렬을 하는 .rjust(n) 사용

# sol3 재귀 이용하기


def solution(n, x):
    N = x
    if n <= 1:
        return n
    # 공백은, n이 4, 3, 2, 1, 0
    # 별은, x가 1, 2, 3, 4, 5 이렇게 되면 된다.
    print(' '*(N-n)+'*'*solution(n-1, N))
    return n


n = int(input())
solution(n+1, n+1)
