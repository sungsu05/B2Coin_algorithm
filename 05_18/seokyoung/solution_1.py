import sys
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# N = N * "*"
# N = 5

# print(N*'*') #*****
input = sys.stdin.readline
for i in range(1, int(input())+1):
    i = i*'*'
    print(i)
    # 입력값이 몇개들어올지 모르는 문제에 readline을 쓰면 좋을듯
    