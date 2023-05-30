# 성택이의 은밀한 비밀번호

import sys
input = sys.stdin.readline

N = int(input())
strings = []
for _ in range(N):
    strings.append(input())

# print(strings) # ['asdf\n', 'asdfghh\n', 'asdfhhjjjj\n']
# print(len(strings[0])) # 5

for i in strings:
    if len(i) >= 7 and len(i) <= 10:
        print("yes")
    else:
        print("no")