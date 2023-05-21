# import sys
# N = int(sys.stdin.readline().rstrip())
# for i in range(1, N+1):
#     print(" " * (N - i) + "*" * i)

import sys
M = int(sys.stdin.readline().rstrip())
for i in range(1, M+1):
    print(("*" * i).rjust(M))
