# 별찍기 8

import sys
input = sys.stdin.readline

N = int(input())

# sol1
for i in range(N):
    star = '*'*(i+1)
    print(star.ljust(N)+star.rjust(N))
    
for i in range(N-1):
    star = '*'*(N-1-i)
    print(star.ljust(N)+star.rjust(N))