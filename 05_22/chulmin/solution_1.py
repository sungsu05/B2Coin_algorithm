import re
import sys
N = int(input())
for _ in range(N):
    A = sys.stdin.readline().rstrip()
    try:
        if re.search(r"[a-zA-Z0-9]{6,9}", A).group() == A:
            print("yes")
        else:
            print("no")
    except:
        print("no")
