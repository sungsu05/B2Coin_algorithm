import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    flag = 0
    commands = list(sys.stdin.readline().rstrip())
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        num_list = deque(map(int, sys.stdin.readline().rstrip().lstrip(
            '[').rstrip(']').split(',')))
    else:
        sys.stdin.readline().rstrip().rstrip()
        num_list = deque()

    direction = 0

    for command in commands:
        if command == 'R':
            if direction == 1:
                direction = 0
            else:
                direction = 1

        elif command == 'D':
            try:
                if direction == 0:
                    num_list.popleft()
                else:
                    num_list.pop()
            except:
                flag = 1
                print('error')
                break

    if flag == 0:
        if direction == 0:
            print('[' + ','.join(map(str, list(num_list))) + ']')
        else:
            print('[' + ','.join(map(str, reversed(list(num_list)))) + ']')
