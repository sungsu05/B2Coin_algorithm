import sys

stack = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == 'pop':
        try:
            a = stack.pop()
            print(a)
        except:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
