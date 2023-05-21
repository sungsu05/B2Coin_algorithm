# 과녁
t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

length_of_two = ((t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2) ** 0.5

if t1[2] + t2[2] > length_of_two:
    print("YES")
else:
    print("NO")
    
## 주석