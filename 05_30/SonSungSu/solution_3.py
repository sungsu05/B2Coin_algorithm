# https://www.acmicpc.net/problem/2445
# 별찍기 - 8
# n = 5
# i = 0    *        * star 1 sp 4 sp 4 star 1 ,  n - i - 1= 4
# i = 1    **      ** star 2 sp 3 sp 3 star 2 ,  n - i - 1= 3
# i = 2    ***    *** star 3 sp 2 sp 2 star 3 ,  n - i - 1= 2
# i = 3    ****  **** star 4 sp 1 sp 1 star 4 ,  n - i - 1= 1
# i = 4    ********** star 5 sp 0 sp 0 star 5 ,  n - i - 1= 0


# i = 1    ****  **** star 4 sp 1 sp 1 star 4 ,  n - i - 1= 4
# i = 2    ***    *** star 3 sp 2 sp 2 star 3 ,  n - i - 1= 3
# i = 3    **      ** star 2 sp 3 sp 3 star 2 ,  n - i - 1= 2
# i = 4    *        * star 1 sp 4 sp 4 star 1 ,  n - i - 1= 1

# input = n
# sum(i) = (n - 1) + (n - 2)
# top left,right star = i + 1
# top left,right sp = n - i -1

# bottom left,right star = n - i -1
# bottom left,right sp = i + 1

def solution(x, y):
    return ("*" * x) + (" " * (y + y)) + ("*" * x)


n = int(input())
for i in range(n):
    print(solution(i + 1, n - i - 1))
for i in range(n):
    print(solution(n - i - 1, i + 1))
