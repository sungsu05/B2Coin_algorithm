import sys
N = int(input())
dance = set()
flag = 0
for _ in range(N):
    candidate = sys.stdin.readline().rstrip().split()
    if candidate[0] == 'ChongChong' or candidate[1] == 'ChongChong':
        flag = 1
        dance.add(candidate[0])
        dance.add(candidate[1])

    if flag == 1:
        if candidate[0] in dance or candidate[1] in dance:
            dance.add(candidate[0])
            dance.add(candidate[1])

print(len(dance))
