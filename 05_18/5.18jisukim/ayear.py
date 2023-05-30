# 윤년
import sys
input = sys.stdin.readline

m = int(input())
if (m % 4 == 0) and (m % 100 != 0 or m % 400 == 0):
    print(1)
else:
    print(0)
