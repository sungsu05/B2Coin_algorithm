# 별짓기 7
import sys
input = sys.stdin.readline

N = int(input())

# sol)
for i in range(1,N):
    print(' '*(N-i) + '*'*(2*i-1))

for i in range(N,0,-1):
    print(' '*(N-i) + '*'*(2*i-1))


# sol2)
for i in range(1,N):
    print(' '*(N-i) + '*'*(2*i-1))

for i in reversed(range(1,N)):
    print(' '*(N-i) + '*'*(2*i-1))


# sol3) 재귀

# 4 1 
# 3 3 
# 2 5  
# 1 7 
# 0 9 

def solution(n,i):
    if n-i < 0:
        return 0
    print(' '*(n-i) + '*'*(2*i-1))
    solution(n,i+1)
    if n-1 != 0:
        print(' '*(n-i+1) + '*'*(2*i-3))
        
n = int(input())
solution(n,1)
