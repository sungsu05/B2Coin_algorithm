# 스택
import sys; 
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    inputstr = input().split()
    order = inputstr[0]
    
    if order == 'push':
        stack.append(inputstr[1])
    
    if order == 'top' and len(stack)!=0:
        print(stack[-1])
    elif order == 'top' and len(stack) ==0:
        print(-1)
    
    if order == 'size':
        print(len(stack))
    
    if order == 'empty':
        print(1) if len(stack)==0 else print(0)
        
    if order == 'pop' and len(stack) != 0:
        print(stack.pop())
    elif order == 'pop' and len(stack) ==0:
        print(-1)
                    