# 별찍기 https://www.acmicpc.net/problem/2444
"""
    *       star = 1   , sp = 4
   ***      star = 3   , sp = 3
  *****     star = 5   , sp = 2
 *******    star = 7   , sp = 1
*********   star = 9   , sp = 0

 *******    star = 5   , sp = 1
  *****     star = 3   , sp = 2
   ***      star = 2   , sp = 3
    *       star = 1   , sp = 4
"""


def solution(n,i):
    if n <= 0:
        return n
    print(" "*(n-1)+"*"*(i+i-1))
    solution(n-1,i+1)
    if n != 1:
        print(" "*(n-1)+"*"*(i+i-1))
    return n



solution((int(input())),1)