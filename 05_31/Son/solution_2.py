# 스택 https://www.acmicpc.net/problem/10828



"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
box =[]
for i in range(int(input())):
    str = sys.stdin.readline().rstrip().split(' ')
    if str[0] == "push":
       box.append(str[1])
    elif str[0] == "pop":
        try:
            print(box.pop())
        except IndexError:
            print(-1)
    elif str[0] == "size":
        print(len(box))
    elif str[0] == "empty":
        print(0 if(len(box)) else 1)
    else:
        print(box[-1] if len(box) else -1)