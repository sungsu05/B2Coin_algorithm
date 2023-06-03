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
        
# word = input().rstrip()
# print(word == 'ENTER') 이러니 False가 나온다.
# print(word, 'ENTER')를 해보니
# 하나는 ENTER 잘 나오고, 하나는 띄어쓰기+ENTER 나온다.
# input()의 결과값 뒤에 개행문자 \n이 추가되서인듯
