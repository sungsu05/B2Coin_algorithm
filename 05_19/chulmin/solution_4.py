from datetime import datetime

# 개선 전 코드
N = 100000000
sieve = [True for _ in range(N + 1)]
sieve[0] = sieve[1] = False

past = datetime.now()
for i in range(2, int(N ** 0.5) + 1):
    for j in range(i * 2, N + 1, i):
        sieve[j] = False

print(sieve.count(True))
print(datetime.now() - past)


# 개선 후 코드
N = 100000000
chae = [True for _ in range(N + 1)]
chae[0] = chae[1] = False

past = datetime.now()
for i in range(2, int(N ** 0.5) + 1):
    if chae[i] == True:
        for j in range(i * i, N + 1, i):
            chae[j] = False

print(chae.count(True))
print(datetime.now() - past)


# N = int(input())
# numbers = map(int, input().split())

# count = 0

# for k in numbers:
#     if chae[k]:
#         count += 1
# print(count)


# N = int(input())

# number_list = map(int, input().split())

# count = 0

# for i in number_list:
#     flag = 0
#     if i == 1:
#         flag = 1
#     for j in range(2, i):
#         if i % j == 0:
#             flag = 1
    
#     if flag == 0:
#         count += 1

# print(count)