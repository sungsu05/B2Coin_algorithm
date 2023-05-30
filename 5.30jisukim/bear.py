# 인사성 밝은 곰곰이

# sol1 집합
import sys
input = sys.stdin.readline

N= int(input())
cnt = 0 
inputset = set()

for _ in range(N):
    word = input()[:-1]
    # print(word =='ENTER') # True 나옴
    if word != 'ENTER':
        if word not in inputset:
            cnt += 1
        inputset.add(word)
    else:
        inputset.clear()

print(cnt)
        
# word = input()
# print(word == 'ENTER') 이러니 False가 나온다.\
# 이유는 word 뒤에 줄바꿈이 들어가서인듯.. '/n'