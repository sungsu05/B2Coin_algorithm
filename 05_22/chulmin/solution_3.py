import sys
N = int(sys.stdin.readline().rstrip())
for i in range(1, 2 * N):
    if i <= N:
        i = i
    else:
        i = 2 * N - i
    print("*" * i + " " * (2 * (N - i)) + "*" * i)
