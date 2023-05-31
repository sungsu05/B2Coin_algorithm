# 붙임성 좋은 총총이

# sol1
import sys; 
input = sys.stdin.readline

danceset = {'ChongChong'}
N = int(input())

for _ in range(N):
    a, b = input().split()
    
    if a in danceset:
        danceset.add(b)
    elif b in danceset:
        danceset.add(a)
    else:
        pass

print(len(danceset))

# sol2
import sys; 
input = sys.stdin.readline
from collections import defaultdict

dance = defaultdict(bool)
# 모든 해시에 대해 디폴트 값은 False
dance['ChongChong'] = True
answer = 1

for _ in range(int(input())):
    A, B = input().split()
    if dance[A]:
        if not dance[B]:
            dance[B] = True
            answer += 1
    elif dance[B]:
        dance[A] = True
        answer += 1

print(answer)


# sol1이 44ms, sol2가 64ms 첫번째 방식이 좀 더 빠름