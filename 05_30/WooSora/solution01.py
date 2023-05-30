n = int(input()) 

for i in range(n):
    s = input()   
    if 6 <= len(s) <= 9 and s.isalnum():    # 조건 확인
        print("yes")
    else:
        print("no")