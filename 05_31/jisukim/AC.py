import sys; 
input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())

for _ in range(N):
    order = list(input().rstrip())
    n = int(input())
   
    
    if n == 0:
        input()
        arr = deque()
    else:
        arr = deque(map(int, input().rstrip().lstrip(
            '[').rstrip(']').split(',')))
        
    
    noterror = True
    direction = 0
    for i in order:
        if i == 'R':
            if direction == 1:
                direction = 0
            else:
                direction = 1
        elif i == 'D':
            try:
                if direction == 0:
                    arr.popleft()
                else:
                    arr.pop()
            except:
                noterror = False
                print('error')
                break
            
    if noterror:
        if direction == 0:
            print("["+ ",".join(map(str, list(arr))) +"]")
        else:
            print("["+ ",".join(map(str, reversed(list(arr)))) +"]")
        
    