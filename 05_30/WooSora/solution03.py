#별찍기

n = int(input())

for i in range(1, n+1):
    print("*" * i + " " * (2*n - 2*i) + "*" * i)
for i in reversed(range(1, n)):
    print("*" * i + " " * (2*n - 2*i) + "*" * i)
