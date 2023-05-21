# chae = [True for _ in range(1001)]
# chae[0] = chae[1] = False
# for i in range(2, int(1000 * 0.5) + 1):
#     for j in range(i * i, 1001, i):
#         chae[j] = False

# N = int(input())
# numbers = map(int, input().split())

# count = 0

# for k in numbers:
#     if chae[k]:
#         count += 1
# print(count)


N = int(input())

number_list = map(int, input().split())

count = 0

for i in number_list:
    check = 0
    if i == 1:
        check = 1    
    for j in range(2, i):
        if i % j == 0:
            check = 1
    
    if check == 0:
        count += 1

print(count)