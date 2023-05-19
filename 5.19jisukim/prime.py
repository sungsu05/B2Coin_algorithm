# 소수 찾기

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
# print(nums) -> [1, 3, 5, 7]
# nums = map(int,input().split()) -> map object

count = 0
for num in nums:
    error = 0
    if num > 1:
        for x in range(2, num):
            if num % x == 0:
                error = 1
        if error == 0:
            count += 1

print(count)

# # 에라토스테네스의 체


# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n
#     sieve[0] = sieve[1] = False

#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우
#             for j in range(i*2, n, i):  # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 개수 산출
#     print(sieve.count(True))


# prime_list(10)

# 에라토스테네스 체를 이용하여 백준 문제 풀이
sieve = [True]*1000
sieve[0] = sieve[1] = False
for i in range(2, int(1000 ** 0.5) + 1):
    for j in range(i * 2, 1000, i):
        sieve[j] = False

N = int(input())
nums = map(int, input().split())

count = 0

for k in nums:
    if sieve[k]:
        count += 1
print(count)
