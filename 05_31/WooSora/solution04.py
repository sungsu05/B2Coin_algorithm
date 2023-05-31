from collections import deque

t = int(input())

for _ in range(t):
    error = False 
    p = input() 
    n = int(input()) 
    arr = input()[1:-1].split(',') 
    arr = deque(arr)

for i in p:
    if i == 'R':
        arr.reverse()
    else:
        if arr:
            pass #모르겠음
        else:
            error = True
            break

#여기서부터 모르겠어요..ㅋㅋㅠ