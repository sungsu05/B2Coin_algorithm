# 백준 세금 문제
# 전체 상금의 22%를 제세공과금으로 납부
# 상금의 20%중 22%를 제세공과금으로 납부

import sys
input = sys.stdin.readline
n = int(input())

money1 = int(n*(0.78))
money2 = int(n*(1-0.2*0.22))

print(money1, money2)